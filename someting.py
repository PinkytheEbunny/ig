import sys
import random
import requests
p = 0
print("Welcome To The Pokedex!")
while p == 0:  
    choices = input("What would you like to do today?\n 1.) Choose A Random Pokemon \n 2.) Look Up A Pokemon \n 3.) Exit:\n")
    if choices == "1":
        random_id = random.randint(1, 1025)
        random_url = f'https://pokeapi.co/api/v2/pokemon/{random_id}'
        data2 = requests.get(random_url).json()
        pokemon_png = data2["sprites"]["front_default"]
        random_name = data2['name'].capitalize()
        sprite_url = data2['sprites']['front_default']
        print(f"Name: {data2['name'].capitalize()}")
        print(f"ID: {data2['id']}")
        print(f"Height: {data2['height']}")
        print(f"Weight: {data2['weight']}")
        print(f"PNG Sprite URL: {pokemon_png}")

    elif choices == "2":
        try:
            look_up_a_pokemon = input("What pokemon would you like to look up?\n")
            picked_pokemon = f'https://pokeapi.co/api/v2/pokemon/{look_up_a_pokemon}'
            data3 = requests.get(picked_pokemon).json()
            picked_pokemon_png = data3["sprites"]["front_default"]
            picked_name = data3['name'].capitalize()
            sprite_url = data3['sprites']['front_default']
            what_u_wanna_know = input(f"What would you like to know about {look_up_a_pokemon}?\n 1.) Its weight? \n 2.) Its height? \n 3.) Its Id? \n 4.) All of The Above\n")
            if what_u_wanna_know == "1":
                print(f"Weight: {data3['weight']}")
                print(f"PNG Sprite URL: {picked_pokemon_png}")
            elif what_u_wanna_know == "2":
                print(f"Height: {data3['height']}")
                print(f"PNG Sprite URL: {picked_pokemon_png}")
            elif what_u_wanna_know == "3":
                print(f"ID: {data3['id']}")
                print(f"PNG Sprite URL: {picked_pokemon_png}")
            elif what_u_wanna_know == "4":
                print(f"Weight: {data3['weight']}")
                print(f"Height: {data3['height']}")
                print(f"ID: {data3['id']}")
                print(f"PNG Sprite URL: {picked_pokemon_png}")
            else:
                print("That is not a valid choice.")
        except:
            print("That is not a valid pokemon")
    elif choices == "3":
        sys.exit(0)
    else:
        print("Sorry! That is not a choice!")


























# list_of_people = data['people']
# total = 0
# for person in list_of_people:
#     total += 1 

# print(total)
# for person in data['people']:
#     if person['craft'] not in all_crafts:
#         all_crafts.append(person['craft'])

# print("Many people are currently in space")
# print("All those in space are either on one of the following ships:")
# counter = 1
# for craft in all_crafts:
#     print(f"{counter} - {craft}")
#     counter += 1

# user_choice = input("Which spacecraft are you interested in? (choose a number):")
# craft_chosen = all_crafts[int(user_choice) - 1]

# print(f"the current crew of the {craft_chosen} includes:")
# for person in data['people']:
#     if person['craft'] == craft_chosen:
#         print(f" - {person['name']}")