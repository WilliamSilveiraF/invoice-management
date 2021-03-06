from django.utils import timezone
from . import models
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

    def create(data):
        try:
            newCompany = models.Company.objects.create(
                name=data.get('name'),
                ein=data.get('ein'),
                businessStructure=data.get('businessType'),
                address=data.get('address'),
                creationDate=timezone.now(),
                cellphone=data.get('cellphone'),
                active=True
            )

            return newCompany

        except Exception as error:
            print(error)
            return error

class OrderSerializer(serializers.ModelSerializer):
    costumer = CompanySerializer(required=True)
    class Meta:
        model = models.Order
        fields = '__all__'