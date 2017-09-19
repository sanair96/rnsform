import uuid
from django.db import models

# Create your models here.

DESIGNATION_DESC = (
    ('Assistant Professor', 'Assistant Professor'),
    ('Associate Professor','Associate Professor'),
    ('Professor', 'Professor'),
)


class perinfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,)
    doj_rns = models.DateField()
    designation = models.CharField(max_length=100,choices = DESIGNATION_DESC)
    email = models.EmailField(help_text="example@rnsit.ac.in")

    def __str__(self):
        return self.name

class expinfo(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    name_of_company = models.CharField(max_length=100)
    position_in_company = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField()
    def __str__(self):
        return self.name_of_company

class teachinfo(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    name_of_college = models.CharField(max_length=100)
    position_in_college = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    date_of_completion = models.DateField()

class researchinfo(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    name_of_institution = models.CharField(max_length=100)
    area_of_interest = models.CharField(max_length=100,)
    date_of_joining = models.DateField()
    date_of_completion = models.DateField()

class projects(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    name_of_project = models.CharField(max_length=100)
    brief_description = models.TextField()

class papers_published(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100,)
    abstract = models.TextField()
    name_of_journal = models.CharField(max_length=100)
    year_of_publication = models.DateField()
    link_to_paper = models.URLField()

class books(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE, unique=False,primary_key=True)
    name_of_book = models.CharField(max_length=100)
    authors = models.CharField(max_length=100,)
    year_of_publication = models.DateField()

class achievements(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    description = models.TextField()

class areas_of_interest(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    name_of_area = models.CharField(max_length=100)

class overallexp(models.Model):
    idper = models.ForeignKey(perinfo, on_delete=models.CASCADE,unique=False, primary_key=True)
    exp = models.CharField(max_length=100)