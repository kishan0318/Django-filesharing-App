from django.db import models
import uuid
import os
# Create your models here.


class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable= False, default=uuid.uuid4)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True )
    def __str__(self):
        return f"{str(self.pk)} - {self.created_date.date()}"
    
def get_upload_folder_path(instance , filename):
    return os.path.join(str(instance.folder.uid), filename)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_folder_path)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True )

    def __str__(self):
        return f"{str(self.pk)} - {self.folder}"