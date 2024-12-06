from django.urls import path
from django.urls import path

from movie_app import views


urlpatterns=[

    path('',views.login),
    path('login_post',views.login_post),
    path('userpage',views.userpage),
    path('adminpage',views.adminpage),
    path('add_user',views.add_user),
    path('logout',views.logout),
    path('add_user_POST',views.add_user_POST),
    path('view_profile_user',views.view_profile_user),
    path('edit_user_profile/<id>',views.edit_user_profile),
    path('edit_user_profile_POST',views.edit_user_profile_POST),
    path('add_movie_admin',views.add_movie_admin),
    path('add_movie_admin_POST',views.add_movie_admin_POST),
    path('add_movie_user',views.add_movie_user),
    path('add_movie_user_POST',views.add_movie_user_POST),
    path('edit_movie_user/<id>',views.edit_movie_user),
    path('edit_movie_user_POST',views.edit_movie_user_POST),
    path('delete_movie_user/<id>',views.delete_movie_user),
    path('view_movie_user',views.view_movie_user),
    path('sent_rating_user/<id>',views.sent_rating_user),
    path('sent_rating_user_POST',views.sent_rating_user_POST),
    path('sent_review_user',views.sent_review_user),
    path('sent_review_user_POST',views.sent_review_user_POST),
    path('view_search_movie',views.view_search_movie),

    path('delete_movie_admin/<id>',views.delete_movie_admin),
    path('view_user',views.view_user),
    path('delete_user_admin/<id>',views.delete_user_admin),
    path('add_genre_admin',views.add_genre_admin),
    path('add_genre_admin_POST',views.add_genre_admin_POST),
    path('view_movie_admin',views.view_movie_admin),





]



