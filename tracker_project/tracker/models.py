from django.db import models



CARS = (
    ("BMW",'bmw'),
    ("audi","audi"),
    ("siera","siera")
)

ISSUES = (
    ('engine','engines'),
    ('lights','lights'),
    ('door','door'),
    ('fluid','fluid')
)

from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering =['-email']


class Tracker(models.Model):
    car_name = models.CharField(default=None,max_length=30,choices=CARS)
    mileage = models.IntegerField()
    issue = models.CharField(max_length=30,default=None,choices=ISSUES)
    describe_issues = models.CharField(max_length=3000,default=None)
    driver =models.ForeignKey(Driver,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car_name

    class Meta:
        ordering =['-date_added','date_edited']



class Chat(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering =['-date_added','date_edited']