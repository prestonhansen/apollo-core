from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apollo.core.serializers import (UserSerializer, GroupSerializer,
    RoomSerializer, RoomDataSerializer)
from apollo.core.models import Room, RoomData
from apollo.core.permissions import permissions
from apollo.core.permissions import IsOwnerOrReadOnly
import json
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

#todo view for RoomData

class MatchingRooms(APIView):
    """
    View to return all rooms matching the search criteria
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request):
        capacity = int(request.query_params.get('capacity', 0))
        tags = request.query_params.getlist('tags', [])

        json_dec = json.decoder.JSONDecoder()

        #todo: implement partial matches or exact matches (for tags)?
        rooms = [room for room in Room.objects.all()]
        matches = []

        for room in rooms:
            room_tags = json_dec.decode(room.tags)
            print(room_tags)
            if (room.capacity >= capacity
                    and (set(room_tags) & set(tags))):
                matches.append(room)

        print(matches)
        serializer = RoomSerializer(matches, many=True)
        return Response(serializer.data)
                