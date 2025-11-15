from rest_framework import serializers

from .models import  User, Listing, Booking,Review

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model=User
        fields='__all__'
class ListingSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True) 
    class Meta:
        model = Listing
        fields = '__all__'
class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
