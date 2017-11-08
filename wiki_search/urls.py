
from django.conf.urls import url,include
from . import views
urlpatterns = [
	url(r'^$',views.index),
	url(r'^search/',views.search),
	url(r'^regist/',views.regist),
	url(r'^login/',views.login),
	]