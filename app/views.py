from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest 

def sum_double(request: HttpRequest, a: int, b: int) -> HttpResponse:
    if a == b:
        return HttpResponse((a+b)*2)
    else:
        return HttpResponse(a+b)

def alarm_clock(request: HttpRequest, day: int, vac) -> HttpResponse:
    if vac == "False":
        if day > 0 and day < 6:
            return HttpResponse("7:00")
        else:
            return HttpResponse("10:00")
    elif day > 0 and day < 6:
        return HttpResponse("10:00")
    else:
        return HttpResponse("off")


def lucky_sum(request: HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    sum = 0
    if a == 13:
        return HttpResponse(0)
    elif b == 13:
        return HttpResponse(sum + a)
    elif c == 13:
        return HttpResponse(sum + a + b)
    else:
        return HttpResponse(a + b + c)