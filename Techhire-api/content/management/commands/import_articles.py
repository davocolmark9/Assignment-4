from django.core.management.base import BaseCommand
from content.models import Article

class Command(BaseCommand):
    help = 'Imports sample articles into the database'

    def handle(self, *args, **kwargs):
        articles = [
            {"title": "Intro to Python", "content": "Python is great...", "is_premium": False, "source": "TechBlog"},
            {"title": "Advanced Django DRF", "content": "Deep dive into DRF internals...", "is_premium": True, "source": "TechBlog"},
            {"title": "Global Market Trends", "content": "Stocks are up...", "is_premium": False, "source": "FinanceNews"},
            {"title": "Insider Trading Secrets", "content": "Buy low, sell high...", "is_premium": True, "source": "FinanceNews"},
            {"title": "Healthy Eating", "content": "Eat your vegetables...", "is_premium": False, "source": "HealthDaily"},{
            "title": "Django 101",
            "content": "This is the foundation...",
            "is_premium": True,
            "source": "TechBlog"
            }
        ]

        for data in articles:
            Article.objects.get_or_create(**data)
            
        self.stdout.write(self.style.SUCCESS('Successfully imported sample articles.'))