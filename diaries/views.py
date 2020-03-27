from rest_framework import generics
from .models import Diary
from .serializers import DiarySerializer
from .permissions import IsAuthor



class DiaryList(generics.ListCreateAPIView):
    serializer_class = DiarySerializer
    def get_queryset(self):
        user = self.request.user
        return Diary.objects.filter(author=user)


class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthor,)
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
