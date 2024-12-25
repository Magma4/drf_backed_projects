from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    number_of_days_created = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'number_of_days_created']

    def get_number_of_days_created(self, Book):

        return (date.today() - Book.published_date).days