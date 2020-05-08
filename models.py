from django.db import models

# Create your models here.
class Data(models.Model):
    CdPat = models.CharField('Code du patient', max_length= 20, primary_key=True)
    NomPren = models.CharField('Nom et Prénoms', max_length= 50)
    DatEnrol = models.DateField("Date d'enrolement")
    DatDernVisit = models.DateField('Date de dernière visite')
    DatProchRdv = models.DateField('Date de prochain RDV')
    TelPat = models.CharField('Téléphone du Patient', max_length= 20)
    PersSout = models.CharField('Nom de la personne en soutien', max_length= 50)
    TelPerSout = models.CharField('Téléphone de la personne en soutien', max_length=20)
    Cohorte = models.CharField('Cohorte du patient', max_length=5)
    FB=(
        ('0', 'ND'),
        ('1', 'injoignable'),
        ('2', 'joignable mais menace'),
        ('3', 'joignable mais se dit guerit'),
        ('4', 'mauvais contact'),
        ('5', 'pas de contact'),
        ('6', 'en voyage'),
    )
    Feedback = models.CharField('Retour de relance', max_length=1, choices=FB)
    
    def __str__(self):
        return self.CdPat
