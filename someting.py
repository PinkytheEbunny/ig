import sys
import random
import requests

print("Welcome To The Pokedex!")
# Get ONLY Pokemon names
pokemon_url = "https://pokeapi.co/api/v2/pokemon?limit=1025"
all_pokemon = requests.get(pokemon_url).json()["results"]
# Make a list of just the names
pokemon_names = [pokemon["name"] for pokemon in all_pokemon]
while True:
    choices = input(
        "What would you like to do today?\n"
        " 1.) Choose A Random Pokemon\n"
        " 2.) Look Up A Pokemon\n"
        " 3.) Exit:\n"
    )
    if choices == "1":
        random_id = random.randint(1, 1025)
        random_url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
        data2 = requests.get(random_url).json()
        pokemon_png = data2["sprites"]["front_default"]
        print(f"Name: {data2['name'].capitalize()}")
        print(f"ID: {data2['id']}")
        print(f"Height: {data2['height']}")
        print(f"Weight: {data2['weight']}")
        print(f"PNG Sprite URL: {pokemon_png}")
    elif choices == "2":
        look_up_a_pokemon = input(
            "What pokemon would you like to look up?\n"
        ).lower().strip()
        # Check if the name is a real Pokemon
        if look_up_a_pokemon in pokemon_names:
            picked_pokemon = (
                f"https://pokeapi.co/api/v2/pokemon/{look_up_a_pokemon}"
            )
            data3 = requests.get(picked_pokemon).json()
            picked_pokemon_png = data3["sprites"]["front_default"]
            what_u_wanna_know = input(
                f"What would you like to know about "
                f"{look_up_a_pokemon.capitalize()}?\n"
                " 1.) Its weight?\n"
                " 2.) Its height?\n"
                " 3.) Its Id?\n"
                " 4.) All of The Above\n"
            )
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
        else:
            print("\nDid you mean any of these?")
            found_pokemon = False
            for pokemon in pokemon_names:
                if pokemon.startswith(look_up_a_pokemon):
                    print(pokemon.capitalize())
                    found_pokemon = True
            if not found_pokemon:
                print("No Pokemon found starting with that.")
            print("Please put one of the listed Pokemon names in the search.")
    elif choices == "3":
        sys.exit(0)
    else:
        print("Sorry! That is not a choice!")
