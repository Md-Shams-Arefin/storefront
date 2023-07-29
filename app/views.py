from django.shortcuts import render
# from .models import person_collection
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>App is runing...</h1>')


# def add_person(request):
#     records = {
#         "first_name": "John",
#         "last_name": "Smith"
#     }

#     person_collection.insert_one(records)
#     return HttpResponse('New person is added.')


# def get_all_person(request):
#     person = person_collection.find()
#     return HttpResponse(person)

# from django.shortcuts import render
# from .mongo_connection import get_mongo_connection


# def book_list(request):
#     client = get_mongo_connection()
#     db = client['test_mongo']
#     books_collection = db['books']
#     books = books_collection.find()
#     client.close()

#     return render(request, 'book_list.html', context={'books': books})
