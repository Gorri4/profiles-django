from django.shortcuts import render
from myapi.serializers import UserSerializer, ProfileSerializer, JobSerializer, TagsSerializer, ProfileTagsSerializer, JobTagsSerializer
from myapi.models import User, Profile, Job, Tags, ProfileTags, JobTags
from rest_framework import viewsets
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class JobViewset(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class TagsViewset(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class ProfileTagsViewset(viewsets.ModelViewSet):
    queryset = ProfileTags.objects.all()
    serializer_class = ProfileTagsSerializer

class JobTagsViewset(viewsets.ModelViewSet):
    queryset = JobTags.objects.all()
    serializer_class = JobTagsSerializer
