print("Lista zakupów")

shopping_dict = {
    "piekarnia" : ["chleb", "bułki"],
    "warzywniak" : ["marchew", "seler"]
}
shopping_dict["piekarnia"].append("pączek")
shopping_dict["warzywniak"].append("rukola")



for sklep, produkt in shopping_dict.items():
     
    print("Idę do {}, kupuję tu następujące rzeczy: {}".format(sklep.capitalize(), produkt))
