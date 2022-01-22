from Animals import Animal, Mammal, Bird

# Create a list for Animal objects
animals = list()

# Print a welcome message
print("Welcome to the animal generator!")
print("This program creates Animal objects\n")

while True:

    print("Would you like to create a Mammal or a Bird?")
    select_type = input("1. Mammal\n2. Bird\nWhich one would you like to create? ")

    if(select_type == '1'):
        # Ask the user for the animal's type and name
        animal_type = input("\nWhat type of mammal would you like to create? ")
        animal_name = input("What is the mammal's name? ")
        hair_color = input("What color is the mammal's hair? ")

        # Create a new Animal object
        mammal = Mammal(animal_type, animal_name, hair_color)

        # Append the Animal object to the list
        animals.append(mammal)

    else:
        # Ask the user for the animal's type and name
        animal_type = input("\nWhat type of bird would you like to create? ")
        animal_name = input("What is the bird's name? ")
        can_fly = input("Can the bird fly? ")

        # Create a new Animal object
        bird = Bird(animal_type, animal_name, can_fly)

        # Append the Animal object to the list
        animals.append(bird)

    # Ask the user if they would like to continue creating animals
    choice = input("\nWould you like to add more animals (y/n)? ")
    if choice != "y":
        break

# Print a header
print("\nAnimal List:")

# Loop through the list
for animal in animals:
    # Use accessor methods to get each Animal object's information
    animal_name = animal.get_name()
    animal_type = animal.get_animal_type()
    animal_mood = animal.check_mood()

    # Print the Animal object's information
    print(animal_name, "the", animal_type, "is", animal_mood)
