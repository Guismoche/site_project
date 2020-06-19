from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=30, verbose_name= "Nom")

    class Meta:
        verbose_name= "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, verbose_name="Auteur")
    title  = models.CharField(max_length = 200, verbose_name="Titre")
    slug = models.SlugField()
    content = models.TextField(verbose_name="Contenu")
    created_date = models.DateTimeField(default = timezone.now, verbose_name="Date de création")
    published_date = models.DateTimeField(blank=  True, null = True, verbose_name="Date de publication")
    is_publish= models.BooleanField(blank= True, default = False)

    category = models.ForeignKey(Category, default = 1, on_delete=models.CASCADE, verbose_name="Catégorie")

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    def publish(self):

        self.published_date = timezone.now()
        self.is_publish = True
        self.save()


    def __str__(self):

        return self.title



