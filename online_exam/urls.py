from django.conf.urls import url
from django.urls import path , include
from . import views
from django.contrib import admin
from django.contrib import admin
urlpatterns = [
    url(r'^faculty_dashboard/$', views.faculty_dashboard, name='faculty_dashboard'),
    url(r'^faculty_add_course/$', views.faculty_add_course, name='faculty_add_course'),
    url(r'^faculty_add_exam/$', views.faculty_add_exam, name='faculty_add_exam'),
    url(r'^faculty_add_topic/$', views.faculty_add_topic, name='faculty_add_topic'),
    url(r'^faculty_add_subtopic/$', views.faculty_add_subtopic, name='faculty_add_subtopic'),
    url(r'^faculty_add_question/$', views.faculty_add_question, name='faculty_add_question'),
    url(r'^faculty_evaluate/$', views.faculty_evaluate, name='faculty_evaluate'),
    url(r'^faculty_exam_registrations/$', views.faculty_exam_registrations, name='faculty_exam_registrations'),
    url(r'^faculty_modify_course/$', views.faculty_modify_course, name='faculty_modify_course'),
    url(r'^faculty_modify_exam/$', views.faculty_modify_exam, name='faculty_modify_exam'),
    url(r'^faculty_modify_topic/$', views.faculty_modify_topic, name='faculty_modify_topic'),
    url(r'^faculty_modify_subtopic/$', views.faculty_modify_subtopic, name='faculty_modify_subtopic'),
    url(r'^faculty_modify_question/$', views.faculty_modify_question, name='faculty_modify_question'),
    url(r'^faculty_profile/$', views.faculty_profile, name='faculty_profile'),
    url(r'^faculty_update_course/$', views.faculty_update_course, name='faculty_update_course'),
    url(r'^faculty_update_exam/$', views.faculty_update_exam, name='faculty_update_exam'),
    url(r'^faculty_update_topic/$', views.faculty_update_topic, name='faculty_update_topic'),
    url(r'^faculty_update_subtopic/$', views.faculty_update_subtopic, name='faculty_update_subtopic'),
    url(r'^faculty_update_question/$', views.faculty_update_question, name='faculty_update_question'),
    url(r'^faculty_user_registrations/$', views.faculty_user_registrations, name='faculty_user_registrations'),
    url(r'^faculty_view_courses/$', views.faculty_view_courses, name='faculty_view_courses'),
    url(r'^faculty_view_exams/$', views.faculty_view_exams, name='faculty_view_exams'),
    url(r'^faculty_view_topics/$', views.faculty_view_topics, name='faculty_view_topics'),
    url(r'^faculty_view_subtopics/$', views.faculty_view_subtopics, name='faculty_view_subtopics'),
    url(r'^faculty_view_questions/$', views.faculty_view_questions, name='faculty_view_questions'),
    url(r'^faculty_manual_evaluate/$', views.faculty_manual_evaluate, name='faculty_manual_evaluate'),
    url(r'^faculty_register_evaluate/$', views.faculty_register_evaluate, name='faculty_register_evaluate'),
    url(r'^student_dashboard/$', views.student_dashboard, name='student_dashboard'),
    url(r'^student_exams/$', views.student_exams, name='student_exams'),
    url(r'^student_attempt_exam/$', views.student_attempt_exam, name='student_attempt_exam'),
    url(r'^student_approved_exams/$', views.student_approved_exams, name='student_approved_exams'),
    url(r'^student_verify/', views.student_verify, name='student_verify'),
    url(r'^student_profile/$', views.student_profile, name='student_profile'),
    url(r'^student_progress/$', views.student_progress, name='student_progress'),
    url(r'^student_answer_key/$', views.student_answer_key, name='student_answer_key'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
    url(r'^modify_user/$', views.modify_user, name='modify_user'),
    url(r'^authenticate/(?P<token>[A-Za-z0-9_\.-]*)/$', views.authenticate, name='authenticate'),
    url(r'^get_exams_by_course/$', views.get_exams_by_course, name='get_exams_by_course'),
    url(r'^get_subtopics_by_topic/$', views.get_subtopics_by_topic, name='get_subtopics_by_topic'),
     
    path('', views.home,name="home"),
    path('videos/', views.videos,name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact,name="contact"),
    path('inorganic/', views.inorganic,name="inorganic"),
    path('organic/', views.organic,name="organic"),
    path('physical/', views.physical,name="physical"),
    path('book/', views.book,name="book"),
    path('addvideo/', views.addvideo,name="addvideo"),
    path('search/',views.search,name="search")
    
    
    ]
    



