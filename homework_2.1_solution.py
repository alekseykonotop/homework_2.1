from pprint import pprint

# cook_book_dict = {
#     'dish_1' : [
#         {'ingridient_name': 'name', 'quantity': value, 'measure': 'text'},
#         {'ingridient_name': 'name', 'quantity': value, 'measure': 'text'},
#         {'ingridient_name': 'name', 'quantity': value, 'measure': 'text'}
#         ],
#     'dish_2' : [
#         {'ingridient_name': 'name', 'quantity': value, 'measure': 'text'},
#         {'ingridient_name': 'name', 'quantity': value, 'measure': 'text'},
#         {'ingridient_name': 'name', 'quantity': value, 'measure': 'text'}
#         ],
# }


def create_cook_book_dict():
    cook_book_dict = {}
    with open('cook_book.txt') as f:
        for line in f:
            ingredient_list = []
            dish_in_cook_book = line.strip()
            count_ingridient = int(f.readline().strip())
            for i in range(count_ingridient):
                ingredient_dict = {}
                ingridient_line = f.readline().strip().split(' | ')  # получили список
                ingredient_dict['ingridient_name'] = ingridient_line[0]
                ingredient_dict['quantity'] = int(ingridient_line[1])
                ingredient_dict['measure'] = ingridient_line[2]
                ingredient_list = ingredient_list + [ingredient_dict]
            # print(ingredient_list)
            f.readline()
            cook_book_dict[dish_in_cook_book] = ingredient_list
        return cook_book_dict



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = create_cook_book_dict()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    print(shop_list)
    # for dish, dish_ingridients in cook_book.items():
    # for dish in dishes:
    #     if dish == dish_in_cook_book:
    #         if ingridient_line[0] in shop_list:
    #             shop_list[ingridient_line[0]]['quantity'] += int(ingridient_line[1]) * person_count
    #         else:
    #             new_shop_list_item['ingridient_name'] = ingridient_line[0]
    #             new_shop_list_item['quantity'] = int(ingridient_line[1]) * person_count
    #             new_shop_list_item['measure'] = ingridient_line[2]
    #             shop_list[ingridient_line[0]] = new_shop_list_item  #
    return (shop_list)


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите колличество человек: ', ))
    dishes = input('Введите блюда в расчете на одного человека через запятую, без пробеллов: ', ).lower().split(',')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
