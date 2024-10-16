from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# --- return the books ---
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializerData = BookSerializer(books, many=True).data
    return Response(serializerData)
    
# --- create a new book ---
@api_view(['POST'])
def create_book(request):
    data = request.data
    serializer = BookSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    