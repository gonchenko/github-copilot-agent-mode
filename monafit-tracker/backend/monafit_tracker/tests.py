import os
from django.apps import apps
from django.conf import settings

# Ensure the DJANGO_SETTINGS_MODULE is set for tests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monafit_tracker.settings')

# Ensure apps are loaded before running tests
apps.populate(settings.INSTALLED_APPS)

from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to MonaFit Tracker')