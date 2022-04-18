from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone

from .models import Article
from .views import HomePageView, ArticleCategoryList, ArticleList, ArticleDetail

time = timezone.now()


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)


class ArticleTests(TestCase):
    def test_article_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_url_resolves_article_view(self):
        view = resolve('/articles')
        self.assertEquals(view.func.view_class, ArticleList)


class ArticleCategoryTests(TestCase):
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('articles',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_category_url_resolves_category_view(self):
        view = resolve('/articles/category/articles')
        self.assertEquals(view.func.view_class, ArticleCategoryList)


class ArticleDetailTests(TestCase):
    def setUp(self):
        Article.objects.create(pub_date=time, slug='articles')

    def test_article_detail_view_status_code(self):
        url = reverse('news-detail',
                      kwargs={'year': time.strftime("%Y"),
                              'month': time.strftime("%m"),
                              'day': time.strftime("%d"),
                              'slug': 'articles',
                              })
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_detail_url_resolves_article_detail_view(self):
        view = resolve('/articles/2022/04/18/articles')
        self.assertEquals(view.func.view_class, ArticleDetail)

