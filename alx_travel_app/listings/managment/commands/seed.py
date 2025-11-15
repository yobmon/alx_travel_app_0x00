from django.core.management.base import BaseCommand
from listings.models import User, Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Optional: clear existing listings
        Listing.objects.all().delete()

        # Make sure there are some users
        if User.objects.count() == 0:
            for _ in range(5):
                User.objects.create(
                    name=fake.name(),
                    email=fake.unique.email(),
                    password='password123'  # For testing only
                )

        users = list(User.objects.all())

        # Create 20 sample listings
        for _ in range(20):
            Listing.objects.create(
                owner=random.choice(users),
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                price=random.randint(50, 500),
                location=fake.city()
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
