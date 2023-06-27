from django.db import models

class Foret(models.Model):
    nom = models.CharField(max_length=200, primary_key=True)
    superficie = models.FloatField(help_text="Superficie en hectares (ha)")
    
    def __str__(self):
        return f"{self.nom}"

class Arbre(models.Model):
    id = models.AutoField(primary_key=True)
    coordonnees = models.CharField(max_length=200)
    espece = models.CharField(max_length=200)
    circonference = models.CharField(max_length=50, help_text="Circonférence en (cm)")
    hauteur = models.CharField(max_length=50, help_text="Hauteur en (m)")
    foret = models.ForeignKey(Foret, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Arbre {self.id} - Foret: {self.foret.nom}"
# Create your models here.
