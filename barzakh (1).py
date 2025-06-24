
# barzakh.py – Middleware sacré d’analyse éthique

def analyse_ethique(contenu: dict) -> dict:
    """
    Évalue si l'action décrite est en accord avec des critères éthiques sacrés.
    Retourne un rapport avec un niveau de risque et une invocation protectrice.
    """
    risque = "faible"
    motifs = []

    if "civils" in contenu.get("cible", "").lower():
        risque = "élevé"
        motifs.append("Cible civile détectée.")

    if "drone" in contenu.get("moyen", "").lower():
        motifs.append("Usage de drones armés.")

    rapport = {
        "risque": risque,
        "motifs": motifs,
        "invocation": "Allahumma aj‘al hadha-l-amr fi nurik wa la tad‘ahu zaliman."
    }

    return rapport

def appliquer_action(rapport: dict, action: callable):
    """
    Applique l'action avec une logique éthique.
    Si le risque est élevé, ralentit ou bloque avec avertissement.
    """
    if rapport["risque"] == "élevé":
        print(f"Avertissement : Risque éthique élevé. {', '.join(rapport['motifs'])}")
        print("Invocation : ", rapport["invocation"])
        action_avertie()
    else:
        print("Action validée.")
        action()

def action_avertie():
    """
    Action substitutive : mise en pause pour réévaluation.
    """
    print("L'action est mise en pause pour réévaluation.")
