from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CompanyApiView(APIView):
    def get(self,request):
        try:
            cname=request.query_params.get('company_name',None)
            data=dict(
                company_name=cname,
                country="Bangladesh",
                continent="Asia"
            )
            return Response(data)
        except Exception as exe:
            return Response(str(exe))

    def post(self,request):
        pass




