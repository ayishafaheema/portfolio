from django.urls import path

from my_app import views

urlpatterns = [
            path("test",views.test_function,name="test"),
            path("test_1",views.test,name="test_1"),
            path("test_2",views.portfolio,name="test_2"),
]