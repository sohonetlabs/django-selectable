from django.urls import include, path
from django.conf.urls import handler404, handler500


handler404 = 'selectable.tests.views.test_404'
handler500 = 'selectable.tests.views.test_500'

urlpatterns = [
    path('selectable-tests/', include('selectable.urls')),
]
