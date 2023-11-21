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
    return [food["name"] for food in spicy_foods]

def custom_sort(food):
    return food["heat_level"]

def get_spiciest_foods(spicy_foods):
    filtered_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return sorted(filtered_foods, key=custom_sort, reverse=True)

print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
     for food in get_spiciest_foods(spicy_foods):
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
         

print(print_spiciest_foods(spicy_foods))
    

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    
    return round(average_heat)

print(get_average_heat_level(spicy_foods))

spicy_food = {
                "name": 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            }

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
print(create_spicy_food(spicy_foods, spicy_food))