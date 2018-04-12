# 1. Проходим по всем строкам файла
# 2. Первая строка - название блюда
# 3. Следующая строка - значение 'n' кол-ва строк с ингредиентами этого блюда
# 3.0 Строку преобразовать в список lst = ['яйцо', '2', 'шт.']
# --- Первый элемент в строке - название ингредиента 'ingridient_name'
# --- Второй элемент в строке - колличество 'quantity'
# --- Третий элемент в строке - единица измерения 'measure'
# 4. После 'n' строк - пустая строка
# 5. Возвращаемся на шаг 2
#



# with open('cook_book.txt', encoding='utf8') as f:
#     for line in f:
#         print(line, end='')


cook_book = {
    'зимний салат': [
        {'ingridient_name': 'картофель', 'quantity': 100, 'measure': 'гр'},
        {'ingridient_name': 'колбаса', 'quantity': 100, 'measure': 'гр'},
        {'ingridient_name': 'майонез', 'quantity': 50, 'measure': 'мл'},
        {'ingridient_name': 'яйца', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'огурцы', 'quantity': 50, 'measure': 'гр'}
    ],
    'пюре с говядиной': [
        {'ingridient_name': 'картофель', 'quantity': 200, 'measure': 'гр'},
        {'ingridient_name': 'говядина', 'quantity': 200, 'measure': 'гр'},
        {'ingridient_name': 'масло', 'quantity': 50, 'measure': 'гр'},
    ],
    'торт': [
        {'ingridient_name': 'печенье', 'quantity': 300, 'measure': 'гр'},
        {'ingridient_name': 'сметана', 'quantity': 300, 'measure': 'мл'},
        {'ingridient_name': 'сгущенка', 'quantity': 50, 'measure': 'мл'},
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    # for dish in dishes:
    #     for ingridient in cook_book[dish]:
    #         new_shop_list_item = dict(ingridient)
    #         new_shop_list_item['quantity'] *= person_count
    #         if new_shop_list_item['ingridient_name'] not in shop_list:
    #             shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
    #         else:
    #             shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    # print(shop_list)

with open('cook_book.txt') as f:
    for line in f:
        dish = line.strip()
        count_line = f.readline().strip()
        count_ingridient = int(count_line)
        print('count_ingridient', count_ingridient)
        ingridient_lst = []
        while count_ingridient != 0:
            ingridient_line = f.readline().strip().split(' | ') # Разбил строку на список и удалил ' | '
            print('ingridient_line', ingridient_line) # отладочный принт
            count_ingridient -= 1
        f.readline()




    # return (shop_list)




def print_shop_list(shop_list):
    # Один из вариантов вывода удобночитаемой информации
    # for shop_list_item in shop_list.values():
    #   print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
    # Ниже более простой вариант
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите колличество человек: ', ))

    dishes = input('Введите блюда в расчете на одного человека через запятую, без пробеллов: ', ).lower().split(
        ',')  # .lower() - приводит все строки с нижнему регистру / .split(',') - убирает разделитель между введенными данными и переводит все в список;
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


# create_shop_list()
