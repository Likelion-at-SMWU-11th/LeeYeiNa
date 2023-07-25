from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import url_view, url_parameter_view, function_view, index
from posts.views import class_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # Function Based View
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    # Class Based View
    path('cbv/', class_view.as_view()),  # as_view: 진입 메소드

    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
# 이미지 파일들이 설정된 폴더에 생성
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)