cos_cumparaturi = {
    "client": "Timur",
    "produse": [],
    "total": 0
}

produs1 = {"nume": "Paine", "pret": 4.5, "cantitate": 2}
produs2 = {"nume": "Lapte", "pret": 6.0, "cantitate": 1}
produs3 = {"nume": "Oua", "pret": 12.0, "cantitate": 1}

cos_cumparaturi["produse"].extend([produs1, produs2, produs3])

total = 0
for produse in cos_cumparaturi["produse"]:
    total += produse["pret"] * produse["cantitate"]

cos_cumparaturi["total"] = total
print("Total initial:", cos_cumparaturi["total"])

items = produse.items()
print("\nProduse în coș:")
for produse in cos_cumparaturi["produse"]:
  for key, value in produse.items():
    print(f"{key}:{value}")
cos_cumparaturi["produse"][0]["cantitate"] = 3

total = 0
for produs in cos_cumparaturi["produse"]:
    total += produs["pret"] * produs["cantitate"]

cos_cumparaturi["total"] = total
print("\nTotal după modificare:", cos_cumparaturi["total"])
