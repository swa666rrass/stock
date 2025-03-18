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
    product_price = input("Zadej cenu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)


def search_product():
    possible_product = input("Zadej název produktu:")
    if possible_product in products:
        print(f"Nalezen: {possible_product}")
        menu()
    else:
        print("Produkt nebyl nalezen")
        menu()


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky\n")

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
        search_product()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
