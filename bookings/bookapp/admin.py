from django.contrib import admin
from .models import Bus, Seat, Booking

class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_name', 'bus_number', 'origin', 'destination', 'departure_time', 'arrival_time', 'price')

class SeatAdmin(admin.ModelAdmin):
    list_display = ('bus', 'seat_number', 'is_available')
    list_filter = ('bus', 'is_available')
    actions = ['make_available', 'make_unavailable']
    
    def make_available(self, request, queryset):
        updated = queryset.update(is_available=True)
        self.message_user(request, f'{updated} seats marked as available')
    
    def make_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)
        self.message_user(request, f'{updated} seats marked as unavailable')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'bus', 'seat', 'booking_time')

admin.site.register(Bus, BusAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Booking, BookingAdmin)