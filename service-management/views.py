__author__ = 'rakesh.varma'
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from ps import ps

class DetailView(APIView):

    def get(self, request, format = None):
        p = ps()
        if 'filter' in request.GET:
            results = p.getProcess(str(request.GET['filter']))
        else:
            results = p.getProcess()
        return Response(data = results, status = HTTP_200_OK)