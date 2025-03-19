products = [
    {
        "name": "Nivea krém",
        "price": 89,
    },
    {
        "name": "Jelení lůj",
        "price": 35,
    },
    {
        "name": "Old Spice deodorant",
        "price": 99,
    },
    {
        "name": "Sprchový gel Old Spice",
        "price": 70,
    },
    {
        "name": "Burberry Hero parfém 100ml",
        "price": 3599,
    },
    {
        "name": "Versace Eros Flame parfém 300ml",
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

def product_sum():
    print(f"Celková cena všech čísel je {total}")


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
    print("5. Produkt s nejnižší cenou")
    print("6. Produkt s nejvyšší cenou")
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
        print("Vyhledej produkt")
        #possible_products()

    elif choice == 4:
        product_sum()
        #summary = products['price']
        #print(f"Celková cena produktů je {total}Kč")

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

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
