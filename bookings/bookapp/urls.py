from django.urls import path
from .views import (
    RegisterView, LoginView, BusListCreateView, UserBookingsView, 
    BookingView, BusDetailView, update_seat_availability, delete_booking
)

urlpatterns = [
    path('busses/', BusListCreateView.as_view(), name='buslist'),
    path('busses/<int:pk>/', BusDetailView.as_view(), name='bus-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:user_id>/bookings/', UserBookingsView.as_view(), name='user-bookings'),
    path('booking/', BookingView.as_view(), name='bookings'),
    path('seats/<int:seat_id>/', update_seat_availability, name='update-seat'),
    path('booking/<int:booking_id>/', delete_booking, name='delete-booking'),
]