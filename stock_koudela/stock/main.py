products = [
    {
        "name": "Nivea krém",
        "price": 89,
    },
    {
        "name": "jelení lůj",
        "price": 35,
    },
    {
        "name": "Old spice deodorant",
        "price": 99,
    },
    {
        "name": "Old spice sprchový gel",
        "price": 70,
    },
    {
        "name": "Burberry hero parfém 100ml",
        "price": 3599,
    },
    {
        "name": "Versace eros flame parfém 300ml",
        "price": 7000,
    },
    {
        "name": "Garnier vlasový šampon",
        "price": 120,
    },
    {
        "name": "Adidas sprchový gel all-in-one",
        "price": 35,
    },
    {
        "name": "Krém na ruce",
        "price": 70,
    }
]

def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, Cena: {product['price']}Kč")


def add_product():
    product_name = input("Název produktu:")
    product_price = int(input("Zadej cenu:"))
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)

def searcher(prefix, arr):

    return [product for product in arr if prefix.lower() in product["name"].lower()]

def search_printer(found):

    if found:
        print("\nNalezené položky:")
        for product in found:
            print(f"Byl nalezen produkt: {product['name']}, S cenou: {product['price']} Kč")
    else:
        print("Žádné položky nebyly nalezeny.")

def average_price(products):

    total_price = sum(product["price"] for product in products)
    return total_price / len(products)

def edit_product(products):
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]['name']} - {products[i]['price']} Kč")

    choice = int(input("Zadej číslo produktu, který chceš upravit: "))

    new_name = input("Zadej nový název: ")
    new_price = int(input("Zadej novou cenu: ")) -1

    products[choice]["name"] = new_name
    products[choice]["price"] = new_price

    print("Produkt byl upraven!")


def product_sum():
    total = 0
    for product in products:
        total += product['price']

    print(f"Celková cena všech produktů je {total}Kč")


def max_price():
    max_product = products[0]

    for product in products[1:]:

        if product["price"] > max_product["price"]:
            max_product = product

    return max_product

"""
Shorter version
def max_price():
    max_product = max(products, key=lambda product: product['price'])
    print(f"Produkt s nejvyšší cenou je {max_product['name']} za {max_product['price']} Kč.")
"""

def min_price():
    min_product = products[0]

    for product in products[1:]:

        if product["price"] < min_product["price"]:
            min_product = product

    return min_product

"""
Shorter version
def min_price():
    min_product = min(products, key=lambda product: product['price'])
    print(f"Produkt s nejnižší cenou je {min_product['name']} za {min_product['price']} Kč.")
"""


def menu():
    print("Vítej ve skladu")
    print("###############")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky")
    print("4. Celková suma cen")
    print("5. Produkt s nejnižší cennou")
    print("6. Produkt s nejvyšší cennou")
    print("7. Průměr všech cen")
    print("8. Úprava produktu")
    print("###############\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Vyhledej produkt podle názvu")
        user_prefix = input("Zadejte část názvu: ").strip().lower()
        found = searcher(user_prefix, products)
        search_printer(found)
        menu()

    elif choice == 4:
        product_sum()
        print("")
        menu()

    elif choice == 5:
        print("Nejlevnější produkt je:")
        min_price()
        min_product = min_price()
        print(f"Produkt s nejnižší cenou je {min_product['name']} za {min_product['price']} Kč.")
        print("")
        menu()

    elif choice == 6:
        print("Nejdražší produkt je:")
        max_price()
        max_product = max_price()
        print(f"Produkt s nejvyšší cenou je {max_product['name']} za {max_product['price']} Kč.")
        print("")
        menu()

    elif choice == 7:
        print("Průměr cen všech produktů:")
        print(average_price(products))
        menu()


    elif choice == 8:
        print("Úprava produktu:")
        edit_product(products)
        menu()


    else:
        print("Zadal jsi špatně!\n")
        menu()

menu()

