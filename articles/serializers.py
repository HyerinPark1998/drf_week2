from rest_framework import serializers
from articles.models import Articles


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
