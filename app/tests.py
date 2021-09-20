from django.http import response
from django.test import SimpleTestCase

class TestSumDouble(SimpleTestCase):
    def test_sum_12(self):
        response = self.client.get("/warmup-1/sum_double/1/2/")
        self.assertContains(response, "3")

    def test_sum_33(self):
        response = self.client.get("/warmup-1/sum_double/3/3/")
        self.assertContains(response, "12")

    def test_sum_22(self):
        response = self.client.get("/warmup-1/sum_double/2/2/")
        self.assertContains(response, "8")

class TestAlarmClock(SimpleTestCase):
    def test_alarm_1_False(self):
        response = self.client.get("/logic-1/alarm_clock/1/False/")
        self.assertContains(response, "7:00")

    def test_alarm_0_True(self):
        response = self.client.get("/logic-1/alarm_clock/0/True/")
        self.assertContains(response, "off")

    def test_alarm_5_True(self):
        response = self.client.get("/logic-1/alarm_clock/5/True/")
        self.assertContains(response, "10:00")

class TestLuckySum(SimpleTestCase):
    def test_sum_123(self):
        response = self.client.get("/logic-2/lucky_sum/1/2/3/")
        self.assertContains(response, "6")
    
    def test_sum_13_2_13(self):
        response = self.client.get("/logic-2/lucky_sum/13/2/13/")
        self.assertContains(response, "0")
    
    def test_sum_721(self):
        response = self.client.get("/logic-2/lucky_sum/7/2/1/")
        self.assertContains(response, "10")
