from django.db import models

class PincodeTable(models.Model):
    id = models.AutoField(primary_key=True)
    circlename = models.CharField(max_length=50, db_column='CircleName')
    regionname = models.CharField(max_length=50, db_column='RegionName')
    divisionname = models.CharField(max_length=50, db_column='DivisionName')
    officename = models.CharField(max_length=50, db_column='OfficeName')
    pincode = models.CharField(max_length=50, db_column='Pincode')
    officetype = models.CharField(max_length=50, db_column='OfficeType')
    delivery = models.CharField(max_length=50, db_column='Delivery')
    district = models.CharField(max_length=50, db_column='District')
    statename = models.CharField(max_length=50, db_column='StateName')
    latitude = models.CharField(max_length=50, db_column='Latitude')
    longitude = models.CharField(max_length=50, db_column='Longitude')

    class Meta:
        db_table = 'pincode_table'

    def __str__(self):
        return self.circlename
