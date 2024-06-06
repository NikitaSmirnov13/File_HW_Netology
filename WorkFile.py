from pprint import pprint
#  Задача 1
with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file.read().split('\n\n'):
        meal_name, *ingredients = line.split('\n')
        cook_lst = []
        for ingredient in ingredients[1:]:
            ingredient_name, quantity, measure = ingredient.split('|')
            cook_lst.append(
                {
                    "ingredient_name": ingredient_name,
                    "quantity": int(quantity),
                    "measure": measure
                }
            )

        cook_book[meal_name] = cook_lst
    pprint(f'Ответ на задание 1:{cook_book}')

#  Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    product_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in product_list:
                product_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                product_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count

    return product_list
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print()
pprint(f'Ответ на задание 2 : {result}')




