from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views as core_views

urlpatterns = [
    path('', core_views.HomePageView.as_view(), name='home'),
    path('payment', core_views.PaymentPageView.as_view(), name='payment'),
    path('payment_confirm/', core_views.PaymentConfirmPageView.as_view(), name='payment_confirm'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', core_views.signup, name='signup'),

    path('doctor/entry/', core_views.AddDoctorView, name='doctor-entry'),
    path('doctor/appointment/', core_views.AddAppointment, name='appointment'),
    path('appointment/<int:pk>/delete/', core_views.AppointmentDelete.as_view(), name='delete-appointment'),
    path('list/', core_views.DocListView.as_view(), name='list'),
    path('profile/', core_views.AppointmentListView.as_view(), name='profile'),
    path('doctor/<int:pk>/', core_views.DocDetailView.as_view(), name='doctor'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
