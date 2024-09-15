spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    print([food["name"] for food in spicy_foods])
    return [food["name"] for food in spicy_foods]

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    print(spiciest_foods)
    return spiciest_foods

get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):

    hot_pepper_emoji = '🌶'

    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']

        heat_level_emoji = hot_pepper_emoji * heat_level
        
        print(f'{name} ({cuisine}) | Heat Level: {heat_level_emoji}')

print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        
        if food['cuisine'] == cuisine:
            print(food)
            return food
    return None

get_spicy_food_by_cuisine(spicy_foods, 'Thai')

def print_spiciest_foods(spicy_foods):
    hot_pepper_emoji = '🌶'

    for food in spicy_foods:
        if food['heat_level'] > 5:
            hot_pepper_string = hot_pepper_emoji * food['heat_level']
            name = food['name']
            cuisine = food['cuisine']

            print(f'{name} ({cuisine}) | Heat Level: {hot_pepper_string}')

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
        
    average_heat_level = total_heat_level / len(spicy_foods)
    print(average_heat_level)
    return average_heat_level
    

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):

    spicy_foods.append(spicy_food)
    print(spicy_foods)
    return spicy_foods

create_spicy_food(spicy_foods, {"name": "Pad Thai", "cuisine": "Thai", "heat_level": 7})
    
