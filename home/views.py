from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from home.models import Profile
from home.models import Orders
from home.models import create_user_Profile
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum


def index(request):
     nav_bar_items={"1_navbar_item":"Home","2_navbar_item":"About su","3_navbar_item":"contact-us","4_navbar_item":"Other actions"}
     if request.user.is_anonymous:
          return render(request,'login-signup.html')
     return render(request,'index.html' , nav_bar_items)
     


def about(request):
     nav_bar_items={"1_navbar_item":"Home","2_navbar_item":"About su","3_navbar_item":"contact-us","4_navbar_item":"Other actions"}
     if request.user.is_anonymous:
          return render(request,'login-signup.html')
     return render(request,'about.html' , nav_bar_items)


def contact(request):
     nav_bar_items={"1_navbar_item":"Home","2_navbar_item":"About su","3_navbar_item":"contact-us","4_navbar_item":"Other actions"}
     if request.user.is_anonymous:
          return render(request,'login-signup.html')
     if request.method == 'POST':
          n = request.POST.get('name')
          # p = request.POST.get('phone')
          e = request.POST.get('email')
          d = request.POST.get('desc')
          c = Contact(name = n, email = e , desc = d,date = datetime.today())
          c.save()
          print("Message before submitted")
          messages.success(request, "Form has been submited")
          return render(request,'contact.html', nav_bar_items)
          
     return render(request,'contact.html' , nav_bar_items)

def loginuser(request):
     if request.method == 'POST':
          userN = request.POST.get("username")
          passW = request.POST.get("password")
          user = authenticate(username=userN, password= passW)
          if user is not None:
               login(request,user)
               return redirect("/")
          else:
               messages.warning(request, "Please Login with correct credentials")
               return render(request,'login-signup.html')

     return redirect("/")

def logoutuser(request):
     logout(request)
     return redirect("/login-signup")

def signupuser(request):
     if request.method == 'POST':
          Rname = request.POST.get("registername")
          Rfname = request.POST.get("registerfname")
          Rlname = request.POST.get("registerlname")
          Rpassword= request.POST.get("registerpassword")
          Rre_password = request.POST.get("re-enteredpassword")
          Remail = request.POST.get("registeremail")
          Rph_num = request.POST.get("register_ph_num")

          if Rpassword!=Rre_password:
               messages.warning(request, "ERROR: Password and Re-Entered Password does not Match. Please SignUp again.")
               return redirect("/")


          user = User.objects.create_user(Rname , Remail, Rpassword)
          user.first_name = Rfname
          user.last_name = Rlname
          user.profile.ph_number = Rph_num
          user.profile.account_created_Date = datetime.today()
          user.save()

          messages.success(request,"Account registered")
          return redirect("/login-signup")

     return render(request,"login-signup.html")

def Update_fields(request):
     if request.user.is_anonymous:
          return render(request,'login-signup.html')
     if request.method == 'POST':
          Uname = request.POST.get("updatename")
          Ufname = request.POST.get("updatefname")
          Ulname = request.POST.get("updatelname")
          Uph_num = request.POST.get("update_ph_num")
          Uemail = request.POST.get("updateemail")
          Uadd_line1 = request.POST.get("update_address_line_1")
          Uadd_line2 = request.POST.get("update_address_line_2")
          Upincode = request.POST.get("updatepincode")
          Ucountry = request.POST.get("updatecountry")
          Ustate_or_region = request.POST.get("update_state/region")
          # Upassword= request.POST.get("updatepassword")
          confirm_password = request.POST.get("confirm_password")

          # print(request.user.password)
          # print(confirm_password)
          
          user = authenticate(username=request.user , password= confirm_password)
          if user is None:
               messages.warning(request, "ERROR: Password does not Match current password. Please enter the correct password.")
               return redirect("/update_details")
          else:
               ins = User.objects.filter(username = request.user)[0]
               if Uname != "":
                    ins.username = Uname
               if Ufname != "":
                    ins.first_name = Ufname  
               if Ulname != "":
                    ins.last_name = Ulname
               if Uph_num != "":
                    ins.profile.ph_number = Uph_num
               if Uemail!= "":
                    ins.email = Uemail
               if Uadd_line1 != "":
                    ins.profile.Address_line_1 = Uadd_line1
               if Uadd_line2 != "":
                    ins.profile.Address_line_2 = Uadd_line2
               if Upincode != "":
                    ins.profile.pincode = Upincode
               if Ucountry != "":
                    ins.profile.country = Ucountry
               if Ustate_or_region != "":
                    ins.profile.state_or_region = Ustate_or_region
               
               # if Upassword != "":
               #      ins.set_password = Upassword

               ins.save()


               messages.success(request, "Profile Updated succesfully!")
               return redirect("/update_details")

          
     return render(request,"Update_user.html")

def Update_fields2(request):
     return render(request,"edit user profile.html")

def cart(request):
     return render(request,"cart.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=User.objects.none()
    else:
        allPosts= User.objects.filter(username__icontains=query)
     #    allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)

def product_card(request):
     return render(request,"product card.html")


#MERCHANT_KEY = 'kbzk1DSbJiV_03p5'
#'MID': 'WorldP64425807474247',

#MERCHANT_KEY = 'bKMfNxPPf_QdZppa'
#'MID': 'DIY12386817555501617',

MERCHANT_KEY = 'TKXCejhTUgmeFnQj'
#'MID' : 'LDYxUY86818217872725',

# Testing dummies
# ---------
# Via Mobile
# Mob no. 77777 77777, Password: Paytm12345, OTP: 489871
# ---------

def payment_gateway(request):
     if request.method == 'POST':
          
          fname_pay = request.POST.get('fname_pay','')         
          lname_pay = request.POST.get('lname_pay','')
               
          email_pay = request.POST.get('email_pay','')
          address_pay = request.POST.get('address_pay','')
          city_pay = request.POST.get('city_pay','')
          state_pay = request.POST.get('state_pay','')
          zipcode_pay = request.POST.get('zipcode_pay','')
          phone_pay = request.POST.get('phone_pay','')

          order = Orders( fname_pay=fname_pay, lname_pay=lname_pay, email_pay=email_pay, address_pay=address_pay, city_pay=city_pay,
          state_pay=state_pay, zipcode_pay=zipcode_pay, phone_pay=phone_pay)
          order.save()
          # 1. items_json = request.POST.get('items_json','') 2. items_json=items_json,
          # Request Paytm to transfer amount to your account after payment by user
          param_dict={

            'MID' : 'LDYxUY86818217872725', 
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(40),
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',

          }
          param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
          return  render(request, 'paytm.html', {'param_dict': param_dict})
     return render(request, "payment_gateway.html")



@csrf_exempt
def handlerequest(request):
     # paytm will send u post request here
     form = request.POST
     response_dict = {}
     for i in form.keys():
       response_dict[i] = form[i]
       if i == 'CHECKSUMHASH':
          checksum = form[i]

     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
     if verify:
       if response_dict['RESPCODE'] == '01':
            print('order successful')
       else:
            print('order was not successful because' + response_dict['RESPMSG'])
     return render(request, 'paymentstatus.html', {'response': response_dict})
    