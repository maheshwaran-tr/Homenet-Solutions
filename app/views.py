from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer,ProductSerializer
from .models import Category,Product
from rest_framework import status,serializers

'''
root
admin123
'''

# Create your views here.
@api_view(["GET"])
def testing(request):
    return Response({"Success":"Testing part is working"})


@api_view(["GET"])
def getCategory(request):
    all_Category = Category.objects.all()
    if all_Category:
        serial = CategorySerializer(all_Category,many=True)
        return Response(serial.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["POST"])
def add_student(request):
    student = CategorySerializer(data=request.data)

    # validating for already existing data
    if Category.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This data already exists")

    if student.is_valid():
        student.save()
        return Response(student.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)