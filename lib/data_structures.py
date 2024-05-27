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
    return[food["name"] for food in spicy_foods]
names = get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food["heat_level"]>5]
spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_level_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_emojis}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
     return None  # Return None if no matching cuisine is found
result = get_spicy_food_by_cuisine(spicy_foods, "Sichuan")
print(result)

def print_spiciest_foods(spicy_foods):
    """
    Prints spicy foods with heat level greater than 5 in the specified format.
    """
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_emojis = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
    """
    Calculates the average heat level of spicy foods.
    """
    if not spicy_foods:  # Handle empty list case
        return 0
    
    total_heat_level = 0
    num_foods = len(spicy_foods)
    
    for food in spicy_foods:
        total_heat_level += food['heat_level']
    
    average_heat = total_heat_level / num_foods
    return int(average_heat)  # Returning as integer as specified

avg_heat = get_average_heat_level(spicy_foods)
print(f"Average Heat Level: {avg_heat}")

def create_spicy_food(spicy_foods, spicy_food):
     """
    Adds a new spicy_food to the list of spicy_foods and returns the updated list.
    """
     spicy_foods.append(spicy_food)
     return spicy_foods

# Example usage:
spicy_foods = [
    {'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9},
    {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6},
]

new_food = {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 5}
updated_spicy_foods = create_spicy_food(spicy_foods, new_food)

print("Updated Spicy Foods:")
print(updated_spicy_foods)