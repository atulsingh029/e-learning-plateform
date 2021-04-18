from django.urls import path
from api.views import *

#TODO : standardize all end points
urlpatterns = [
    path('addroom/',add_room),
    path('listallrooms/',list_all_rooms),
    path('listapplications/', list_applications),
    path('acceptapplications/', accept_application),
    path('rejectapplications/', reject_application),
    path('deleteroom/',delete_room),
    path('listallstudents/', list_students),
    path('listroomstudents/<int:room_id>/', list_room_students),
    path('viewroom/<int:room_id>', view_room),
    path('editroom/<int:room_id>', edit_room),
    path('getaccount/<int:id>', get_account),
    path('removestudentfromcurrentroom/<int:id>', remove_student_from_current_room),
    path('changestudentroom/',change_student_room),
    path('listallcourses/',list_all_courses),
    path('addcourse/<str:type>/',add_course),
    path('listallteachers/',list_all_teachers),
    path('opencourse/<str:c_id>/',open_course),
    path('viewstudentroom/',view_student_room),
    path('search/',search),
    path('getbook/<str:id>/', get_book),
    path('deletecourseresource/<str:id>/', delete_resource ),
    path('deletelecture/<str:id>/', delete_lecture ),
    path('addcourseresource/', add_resource),
    path('addlecture/', add_lecture),
    path('editlecture/', edit_lecture),
    path('getteacherscourse', get_teachers_course),

    path('request_live_session/', request_live_session),
    path('get_live_session_requests/', get_live_session_requests),
    path('live_session_request_status/',live_session_request_status),
    path('live_session_scheduler/', live_session_scheduler),
    path('liveclass/offer/<str:id>', live_class_offer_setter),
    path('live_class_get_offer/<str:id>', live_class_get_offer),
    path('liveclass/answer/<str:id>', save_answer),
    path('live_class_get_answer/<str:id>', live_class_get_answer)

]
