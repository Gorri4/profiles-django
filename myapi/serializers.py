from rest_framework import serializers
from myapi.models import User, Profile, Job, Tags, ProfileTags, JobTags

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'description', 'picture_url']

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'description']

class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']

class ProfileTagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProfileTags
        fields = ['profile', 'tag']

class JobTagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobTags
        fields = ['job', 'tag']