from rest_framework import serializers
from .models import Folder , Files
import shutil

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 10000, allow_empty_file = False, use_url = False)
    )
    folder = serializers.CharField(required= False)
    def create_zip(self, folder):
        shutil.make_archive(f"public\\static\\shareable_zip\\{folder}" , 'zip', f"public\\media\\{folder}")
    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        print(files)
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder= folder, file = file)
            files_objs.append(files_obj)
        self.create_zip(str(folder.uid))
        return {'files' : {} , 'folder':  str(folder.uid)}
