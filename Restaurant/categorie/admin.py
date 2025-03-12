from django.contrib import admin 
from categorie.models import Categorie 
class CategorieAdmin(admin.ModelAdmin): 
    list_display = ('desCat', 'imageCat')  # Colonnes affichées dans la liste 
# Enregistrement du modèle Categorie dans l'admin avec la configuration 
CategorieAdmin 
admin.site.register(Categorie, CategorieAdmin) 