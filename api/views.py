from rest_framework import generics, permissions

from .models import AttendanceRecorder
from .serializers import AttendanceRecorderSerializer
from .permissions import SafelistPermission



class AttendanceRecorderListAPIView(generics.ListCreateAPIView):
    serializer_class = AttendanceRecorderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = AttendanceRecorder.objects.all()
        date = self.request.query_params.get('date', None)
        course_id = self.request.query_params.get('course_id', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        if course_id is not None:
            # the character "+", for some reason, disapear in url params
            queryset = queryset.filter(course_id=course_id.replace(" ","+"))
        return queryset.order_by('date')

    
