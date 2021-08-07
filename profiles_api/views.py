from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """ 

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'My Name is Aravind',
            'I am currently working in TCS',
            'I have good knowledge on Python'
        ]

        return Response({'message':'Hello!', 'apiview':an_apiview})