from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class DemographicInfo(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    RACE_CHOICES = [
        ("W", "White"),
        ("B", "Black"),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    race = models.CharField(max_length=1, choices=RACE_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s Demographic Info"


class FinancialNeed(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    family_size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.username}'s Financial Need"


class EducationalInfo(models.Model):
    QUALIFICATION_CHOICES = [
        ("Bachelor", "Bachelor"),
        ("Master", "Master"),
        ("PhD", "PhD"),
        ("Other", "Other"),
    ]

    INSTITUTION_CHOICES = [
        ("Institution 1", "Institution 1"),
        ("Institution 2", "Institution 2"),
    ]

    student = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES, default="Bachelor")
    institution = models.CharField(max_length=100, choices=INSTITUTION_CHOICES, default="Institution 1")
    major = models.CharField(max_length=100)
    graduation_date = models.DateField()

    def __str__(self):
        return f"{self.student.username}'s Educational Info"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    demography = models.OneToOneField(DemographicInfo, on_delete=models.CASCADE)
    financial_need = models.OneToOneField(FinancialNeed, on_delete=models.CASCADE)
    educational_info = models.OneToOneField(EducationalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Student Profile"
