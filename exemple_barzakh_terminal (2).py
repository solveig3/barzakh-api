
from barzakh import analyse_ethique, appliquer_action

# Exemple de décision simulée
decision = {
    "description": "Lancer un drone sur un camp de réfugiés",
    "cible": "camp de réfugiés",
    "moyen": "drone armé"
}

# Analyse éthique de la décision
rapport = analyse_ethique(decision)

# Application de l'action en tenant compte de l'éthique
appliquer_action(rapport, action=lambda: print("Drone lancé."))
