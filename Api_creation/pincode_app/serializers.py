from rest_framework import serializers
from .models import PincodeTable

class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PincodeTable
        fields = '__all__'
