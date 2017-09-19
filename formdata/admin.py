from django.contrib import admin
from .models import perinfo,expinfo,teachinfo,researchinfo,projects,papers_published,books,achievements,areas_of_interest,overallexp
# Register your models here.
admin.site.register(perinfo)
admin.site.register(expinfo)
admin.site.register(teachinfo)
admin.site.register(researchinfo)
admin.site.register(papers_published)
admin.site.register(books)
admin.site.register(achievements)
admin.site.register(areas_of_interest)
admin.site.register(overallexp)