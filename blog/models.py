from django.db import models

# Create a blog models here.

class Blog(models.Model):
    #title
    title = models.CharField(max_length=255)
    #publication date
    pub_date = models.DateTimeField()
    #body/text
    body = models.TextField()
    #image
    image = models.ImageField(upload_to='images/')

#Add the Blog app to the settings.

#Create a migration.

#Migrate.

#Add to the admin
