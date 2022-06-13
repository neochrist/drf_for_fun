from django.test import TestCase
from django.contrib.auth.models import  User

from .models import Post
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        #create user

        testuser1 = User.objects.create_user(username='testuser1', password='abc123')

    # create post

        test_post = Post.objects.create(
            author=testuser1,title='blogtitle', body='blogbody')
        test_post.save()


    def test_post(self):

        post = Post.objects.get(id=1)

        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'


        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'blogtitle')
        self.assertEqual(body, 'blogbody')


