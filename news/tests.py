from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):

    # set up methods
    def setUp(self):
        self.benson = Editor(first_name='Benson',last_name='Langat',email='janja@gmail.com')

    # test instance method
    def test_instance(self):
        self.assertTrue(isinstance(self.benson,Editor))

    # test save methods
    def test_save_method(self):
        self.benson.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ArticleTestClass(TestCase):

    def setUp(self):
        # create a new editor & save
        self.benson = Editor(first_name='Benson',last_name='Langat',email='janja@gmail.com')
        self.benson.save_editor()

        # create a new tag & save it in
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(title='Moringa Tribune',post='Tester content for the Moringa Tribune',editor=self.benson)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all.delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2022-05-21'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
