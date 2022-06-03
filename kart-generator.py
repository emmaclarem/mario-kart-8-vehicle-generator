import random

# introduction
name = input("What's your name? ")
print(f"Hello {name}, let's choose a vehicle for you to race in!")

# character choice dialog
print("Would you like a character chosen for you?")
character_choice = input("Type 'Yes' or 'No' ")

character_list = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser", "Donkey Kong", "Toad", "Koopa Troopa", "Daisy",
                  "Shy Guy", "Wario", "Waluigi", "Baby Mario", "Baby Luigi", "Baby Peach", "Baby Daisy", "Rosalina",
                  "Toadette", "Metal Mario", "Lakitu", "Larry", "Morton", "Wendy", "Iggy", "Roy", "Lemmy", "Ludwig", "Pink Gold Peach", "Baby Rosalina", "Mii", "Tanooki Mario", "Cat Peach", "Link", "Villager", "Isabelle", "Dry Bowser"]
character = ()
if character_choice == 'Yes':
    character = random.choice(character_list)

# vehicle type choice dialog
print("Would you prefer a kart or a bike?")
vehicle_type = input("Type 'Kart', 'Bike', or 'Surprise me' ")

# lists of all kart options
karts_list = ["Standard Kart", "Pipe Frame", "Mach 8", "Steel Driver", "Cat Cruiser", "Circuit Special", "Tri-Speeder", "Bandwagon", "Prancer", "Biddybuggy", "Landship", "Sneeker", "Sports Coupe", "Gold Standard", "Standard ATV", "Wild Wiggler", "Teddy Buggy"]
bikes_list = ["Standard Bike", "Comet", "Sports Bike", "The Duke", "Flame Rider", "Varmint", "Mr. Scooty", "Jet Bike", "Yoshi Bike"]
wheels_list = ["Standard", "Monster", "Roller", "Slim", "Slick", "Metal", "Button", "Off-Road", "Sponge", "Wood", "Cushion", "Blue Standard", "Hot Monster", "Azure Roller", "Crimson Slim", "Cyber Slick", "Retro Off-Road", "Gold Tires"]
gliders_list = ["Super Glider", "Cloud Glider", "Wario Wing", "Waddle Wing", "Peach Parasol", "Parachute", "Parafoil", "Flower Glider", "Bowser Kite", "Plane Glider", "MKTV Parafoil", "Gold Glider"]

# selects vehicle body based on user input
body = ()
if vehicle_type == 'Kart':
    body = random.choice(karts_list)
elif vehicle_type == 'Bike':
    body = random.choice(bikes_list)
elif vehicle_type == 'Surprise me':
    all_vehicle_bodies = karts_list + bikes_list
    body = random.choice(all_vehicle_bodies)
else:
    all_vehicle_bodies = karts_list + bikes_list
    body = random.choice(all_vehicle_bodies)
    print("Oops, I did't quite catch that. I'll choose from all available bodies.")

# selects wheels and glider
wheels = random.choice(wheels_list)
glider = random.choice(gliders_list)

# prints kart choice
print("Here's what you'll be racing with:")
if character != ():
    print(f"Character: {character}")
print(f"Vehicle Body: {body}")
print(f"Wheels: {wheels}")
print(f"Glider: {glider}")
print("On your marks, get set, GO!")

