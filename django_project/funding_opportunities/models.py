from django.db import models
from django.utils.text import slugify

FUNDING_OPPORTUNITY_CATEGORIES = (
    ("Bursary", "Bursary"),
    ("Scholarship", "Scholarship"),
    ("Grant", "Grant"),
)

FIELD_OF_STUDIES = (
    ("Engineering", "Engineering"),
    ("Science", "Science"),
    ("Humanities", "Humanities"),
    ("Social Sciences", "Social Sciences"),
    ("Business", "Business"),
    ("Other", "Other"),
)


SUPPORT_CATEGORIES = (
    ("Tuition", "Tuition"),
    ("Funding", "Funding"),
    ("Other", "Other"),
)

SUPPORTED_INSTITUTIONS = (
    ("Public University", "Public University"),
    ("Private University", "Private University"),
    ("Other", "Other"),
)


class FundingOpportunityCategory(models.Model):
    name = models.CharField(max_length=50, choices=FUNDING_OPPORTUNITY_CATEGORIES)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse


class FundingOpportunity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    eligibility = models.TextField()
    url = models.URLField(blank=True, unique=True)
    close_date = models.DateField()
    field_of_study = models.CharField(max_length=50, choices=FIELD_OF_STUDIES, default="Other")
    institution = models.CharField(max_length=50, choices=SUPPORTED_INSTITUTIONS, default="Other")
    funding_support_category = models.CharField(max_length=50, choices=SUPPORT_CATEGORIES, default="Other")
    category = models.ForeignKey(FundingOpportunityCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
