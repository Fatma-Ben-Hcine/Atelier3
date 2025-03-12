from django.contrib import admin 
from products.models import Products 
class ProductsAdmin(admin.ModelAdmin): 
    list_display = ('title', 'image','previewDescription', 'detailDescription','price', 'qtestock', 'categorie')  # Colonnes affichées dans la liste 
# Enregistrement du modèle Products dans l'admin avec la configuration 
ProductsAdmin 
admin.site.register(Products, ProductsAdmin) 
