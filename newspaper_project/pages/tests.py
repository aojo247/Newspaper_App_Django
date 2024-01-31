from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        """
        Purpose: Test if the home page is accessible and functioning correctly.
        Functionality: Sends a GET request to the root URL ('/') and checks if the
        response status code is 200, indicating the page is accessible without errors.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """
        Purpose: Ensure that the URL for the home page, defined by its name in Django's URL configuration,
        works correctly. Functionality: Uses Django's reverse function to find the URL named 'home', performs a GET
        request to this URL, and checks if the response status code is 200, confirming the URL correctly links to the
        view.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Purpose: Verify that the correct template is used when the home page is rendered. Functionality: Sends a GET
        request to the URL named 'home', confirms the request is successful with a 200 status code, and checks if
        'home.html' template is used in the response.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
    username = 'new_user'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        """
        Purpose: Test if the signup page is accessible and functioning correctly.
        Functionality: Sends a GET request to the signup URL ('/users/signup/') and checks if
        the response status code is 200, indicating the page is accessible without errors.
        """
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """
        Purpose: Ensure that the URL for the signup page, defined by its name in Django's URL configuration,
        works correctly. Functionality: Uses Django's reverse function to find the URL named 'signup', performs a GET
        request to this URL, and checks if the response status code is 200, confirming the URL correctly links to the
        view.
        """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Purpose: Verify that the correct template is used when the signup page is rendered. Functionality: Sends a
        GET request to the URL named 'signup', confirms the request is successful with a 200 status code, and checks
        if 'signup.html' template is used in the response.
        """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        """
        Purpose: Test the functionality of the signup form. Functionality: Creates a new user with a specified
        username and email, then checks if the user is correctly added to the database with the correct username and
        email.
        """
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
