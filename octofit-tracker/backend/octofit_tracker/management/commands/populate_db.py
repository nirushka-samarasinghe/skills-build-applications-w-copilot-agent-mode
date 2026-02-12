
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample teams
        marvel = Team.objects.create(name='Marvel', members=[])
        dc = Team.objects.create(name='DC', members=[])

        # Sample users
        user_data = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
        ]
        for user in user_data:
            User.objects.create(**user)

        # Sample activities
        Activity.objects.create(user='Iron Man', activity='Running', duration=30)
        Activity.objects.create(user='Superman', activity='Swimming', duration=45)
        Activity.objects.create(user='Batman', activity='Cycling', duration=60)

        # Sample leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Sample workouts
        Workout.objects.create(user='Iron Man', workout='Chest', suggestion='Bench Press')
        Workout.objects.create(user='Superman', workout='Legs', suggestion='Squats')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
