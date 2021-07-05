from django.db import models

# Create your models here.



class Products(models.Model):
    category = models.CharField(max_length=50)
    title = models.TextField()
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    rom = models.CharField(max_length=10, null=True, blank=True)
    ram = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    specifications = models.TextField(null=True, blank=True)
    images = models.TextField(null=True, blank=True)
    product_link = models.TextField(null=True, blank=True)
    primary_matched_links = models.TextField(null=True, blank=True)
    secondary_matched_links = models.TextField(null=True, blank=True)
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
        

