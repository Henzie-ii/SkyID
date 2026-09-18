from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def creaate_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email is required")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)

        user.save(using=self.db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields["is_active"]:
            raise ValueError("Super user must have is_staff=True")

        if not extra_fields["is_superuser"]:
            raise ValueError("super user must have is_superuser=True")

        return self.creaate_user(
            email=email,
            password=password,
            **extra_fields,
        )