from EApp import views
from django.conf.urls import url,include
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.conf.urls.static import static
from .views import HomePageView,home

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^home',home,name='home')
 
]