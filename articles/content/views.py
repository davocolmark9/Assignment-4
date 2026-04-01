from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import JobPosting
from .serializers import JobPostingSerializer

class JobListView(generics.ListAPIView):
    queryset = JobPosting.objects.all().order_by('-created_at')
    serializer_class = JobPostingSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['location']


class JobDetailView(generics.RetrieveAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer