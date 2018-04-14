def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    with open('cook_book.txt') as f:
        for line in f:
            dish_in_cook_book = line.strip()
            count_ingridient = int(f.readline().strip())
            while count_ingridient != 0:
                new_shop_list_item = {}
                ingridient_line = f.readline().strip().split(' | ')
                count_ingridient -= 1
                for dish in dishes:
                    if dish == dish_in_cook_book:
                        if ingridient_line[0] in shop_list:
                            shop_list[ingridient_line[0]]['quantity'] += int(ingridient_line[1]) * person_count
                        else:
                            new_shop_list_item['ingridient_name'] = ingridient_line[0]
                            new_shop_list_item['quantity'] = int(ingridient_line[1]) * person_count
                            new_shop_list_item['measure'] = ingridient_line[2]
                            shop_list[ingridient_line[0]] = new_shop_list_item
            f.readline()
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
