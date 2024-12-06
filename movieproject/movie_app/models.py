from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)



class Admin(models.Model):
    LOGIN=models.ForeignKey(Login, on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)




class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)




class Movie(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    # ADMIN=models.ForeignKey(Admin,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_date = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    actors = models.CharField(max_length=255)
    trailerlink = models.CharField(max_length=255)
    image = models.CharField(max_length=100)






class Rating(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    date=models.CharField(max_length=100)

class Review(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    review=models.CharField(max_length=100)







