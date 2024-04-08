
### --------- Type 1 ----------- #####


# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import PincodeTable
# from .serializers import PincodeSerializer

# class PincodeList(viewsets.ModelViewSet):
#     queryset = PincodeTable.objects.all()
#     serializer_class = PincodeSerializer



### --------- Type 2 ----------- #####


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PincodeTable
from .serializers import PincodeSerializer



class PincodeApi(APIView):
    def get(self,request):
        all_datas = PincodeTable.objects.all().values()
        return Response ({"Message":"List of Pincode","Data":all_datas})