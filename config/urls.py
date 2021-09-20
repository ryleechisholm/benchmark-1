from django.contrib import admin
from django.urls import path

from app.views import sum_double, alarm_clock, lucky_sum

urlpatterns = [
    path('admin/', admin.site.urls),
    path("warmup-1/sum_double/<int:a>/<int:b>/", sum_double),
    path("logic-1/alarm_clock/<int:day>/<vac>/", alarm_clock),
    path("logic-2/lucky_sum/<int:a>/<int:b>/<int:c>/", lucky_sum)
]
