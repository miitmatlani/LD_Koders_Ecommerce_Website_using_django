from django.contrib import admin
from django.urls import path,include
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index , name = 'Home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('login-signup', views.loginuser, name = 'login'),
    path('logout', views.logoutuser, name = 'logoout'),
    path('signup', views.signupuser, name = 'signup'),
    path('update_details', views.Update_fields, name = 'Forgot-password'),
    path('update_details2', views.Update_fields2, name = 'Forgot-password'),
    path('search', views.search, name = 'search'),
    path('product_card', views.product_card, name = 'contact2'),
    path('payment_gateway', views.payment_gateway, name = 'payment_gateway'),
    path('handlerequest', views.handlerequest, name = 'Handlerequest'),
    path('cart', views.cart, name = 'cart'),
    ### FOR RESETTING THE PASSWORD
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="forgot password.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete")

]

