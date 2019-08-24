from django.db import models

# Create your models here.


class Company(models.Model):
    """ Compnay Model Class """
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class BusinessUnit(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company,
                                related_name="business_units",
                                on_delete=models.DO_NOTHING)


class Department(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    business_unit = models.ForeignKey(BusinessUnit,
                                      related_name="departments",
                                      on_delete=models.DO_NOTHING)


class Designation(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department,
                                   related_name="designations",
                                   on_delete=models.DO_NOTHING)


class Station(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class Religion(models.Model):
    name = models.CharField(max_length=200)


class MaritalStatus(models.Model):
    name = models.CharField(max_length=200)


class EmploymentType(models.Model):
    name = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_lenght=200)
    description = models.CharField(max_length=2000)
    is_active = models.BooleanField(default=True)
    color = models.CharField(max_length=7, default="#ffffff")


class Dictionary(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 related_name="dictionary_designations")


class Institute(models.Model):
    name = models.CharField(max_length=300)


class EducationLevel(models.Model):
    title = models.CharField(max_length=300)
