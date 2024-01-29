from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    funding_opportunity = models.ForeignKey("funding_opportunities.FundingOpportunity", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "application")

    def __str__(self):
        return self.funding_opportunity
