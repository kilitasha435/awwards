from django.test import TestCase
from . models import *

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id = 1, username = 'Brian', password = 'beta')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))