from django.db import models


# create objects that are mapped to database
class DjangoClasses(models.Model):
    title = models.CharField(max_length=50, null=False)
    course_num = models.IntegerField( blank=True, null=False)
    instructor_name = models.CharField(max_length=50, default="", blank=True, null=False)
    duration = models.FloatField(max_length=5, blank=True, null=False)

    # create model manager
    objects = models.Manager()

    # return when an object is called
    def __str__(self):
        return self.title

#create and save an object
DjangoClasses.objects.create(title='forms', course_num=2343, instructor_name='Snape',duration=23)
DjangoClasses.objects.create(title='migrations', course_num=2292, instructor_name='Mcgonagall',duration=.5)
DjangoClasses.objects.create(title='models', course_num=2983, instructor_name='Sprout',duration=2)
