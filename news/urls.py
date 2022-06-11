from django.urls import re_path,path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.news_of_day,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name='pastNews'),
    path('search/',views.search_results,name='search_results'),
    re_path(r'^article/(\d+)$',views.article,name='article'),
    path('news/article',views.new_article,name='newArticle'),
    path('ajax/newsletter',views.newsletter,name='newsletter'),
    path('api/merch/',views.MerchList.as_view()),
    re_path(r'^api/merch/merch-id/(?P<pk>[0-9]+)/$',views.MerchDescription.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
