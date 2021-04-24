from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = User
        fields = ['url', 'username', 'email']