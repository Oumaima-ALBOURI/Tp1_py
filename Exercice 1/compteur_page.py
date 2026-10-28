
class CompteurPage:
    # Attribut de classe : partagé entre tous les objets
    total_visites = 0

    def __init__(self, nom_page):
        # Attributs d'instance
        self.nom_page = nom_page
        self.visites = 0

        # Incrémenter le compteur global
        CompteurPage.total_visites += 1

    def ajouter_visite(self):
        self.visites += 1
        CompteurPage.total_visites += 1

    def afficher_statistiques(self):
        return f"Page '{self.nom_page}': {self.visites} visites. Total global: {CompteurPage.total_visites}"


# Programme principal
page1 = CompteurPage("Accueil")
page2 = CompteurPage("Contact")

page1.ajouter_visite()
page1.ajouter_visite()
page2.ajouter_visite()

print(page1.afficher_statistiques())
print(page2.afficher_statistiques())
print(CompteurPage.total_visites)
