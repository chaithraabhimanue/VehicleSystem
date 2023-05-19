from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    User_choices=[
        (1, "Super Admin"),
        (2, "Admin"),
        (3, "User"),
    ]
    role=models.PositiveSmallIntegerField(choices=User_choices,default=3)

class Vehicles(models.Model):
    alphanumeric=RegexValidator(r"^[0-9a-zA-Z_]*$",'Only use alphanumeric characters')

    types=[
        ("Two Wheeler","Two Wheeler"),
        ("Three Wheeler","Three Wheeler"),
        ("Four Wheeler","Four Wheeler")
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vehicle_number=models.CharField(max_length=100,validators=[alphanumeric])
    vehicle_type=models.CharField(max_length=100,choices=types,default="two wheeler")
    vehicle_model=models.CharField(max_length=100)
    vehicle_description=models.CharField(max_length=250)


