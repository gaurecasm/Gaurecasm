from django.db import models
# making a custom user model

from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """creates and save new user """
        if not email:
            raise  ValueError('Userrs must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):
        """creates and saves new superuser"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser,PermissionsMixin):
    """custom user model that supports using email insteas of username"""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD= 'email'