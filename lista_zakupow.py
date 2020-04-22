print("Lista zakupów")

shopping_dict = {
    "piekarnia" : ["chleb", "bułki"],
    "warzywniak" : ["marchew", "seler"]
}
shopping_dict["piekarnia"].append("pączek")
shopping_dict["warzywniak"].append("rukola")
shopping_dict["apteka"] = ["apap", "tussipec"]

separator = ", "

for sklep, produkt in shopping_dict.items():
    produkt = [p.capitalize() for p in produkt]
    
    print("Idę do {}, kupuję tu następujące rzeczy: {}".format(sklep.capitalize(), separator.join(produkt)))

piekarnia_count = len(shopping_dict["piekarnia"])
warzywniak_count = len(shopping_dict["warzywniak"])
apteka_count = len(shopping_dict["apteka"])

suma = piekarnia_count + warzywniak_count + apteka_count
print("W sumie kupuję {} produktów.".format(suma))