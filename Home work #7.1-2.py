from collections import Counter
from pprint import pprint

print("Задание №1")
file_name = "recipes.txt"
def catalog_reader(file_name):
    with open(file_name, encoding='utf-8') as file_obj:
        cook_book = {}
        dish = {}
        s = []
        keys = ['ingredient_name', 'quantity', 'measure']
        for line in file_obj:
            dish_name = line.strip()
            goods = []
            quantity = file_obj.readline()
            for item in range(int(quantity)):
                good = file_obj.readline()
                s = good.split()
                good = good.split()
                s.remove("|")
                s.remove("|")
                dish = dict(zip(keys, s))
                goods.append(dish)
            cook_book[dish_name] = goods
            file_obj.readline()
        return cook_book

catalog_reader(file_name)

cook_book = catalog_reader(file_name)
print("cook_book={")
pprint(cook_book,  width=200, indent=1)
print("}")

print()

# Задание №2
print("Задание №2")

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

def get_shop_list_by_dishes(dishes, person_count):
    list_keys = []
    dict_keys = []
    dict_values = {}
    count_dish = Counter(dishes)

    for keys, values in dict(count_dish).items():
        ingredients_dishes = cook_book.setdefault(keys)
        for ingredients in ingredients_dishes:
           ingredients['quantity'] = int(ingredients.get('quantity')) * values
           list_keys.append(ingredients.get('ingredient_name'))
           dict_keys.append(dict(sorted(ingredients.items())))
           dict_values = dict(zip(list_keys, dict_keys))

    for i in dict_keys:
        i['quantity'] = int(i.get('quantity'))*person_count
        del i['ingredient_name']
        # print(i)

    pprint(dict_values)
    return(dict_values)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 3)
