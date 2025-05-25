# virtual_pet.py - Run this file to start the Virtual Pet program.
# No external libraries required. Runs in standard Python environment.

class VirtualPet:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.health = 100

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 5
        if self.happiness > 100:
            self.happiness = 100
        self.health += 2
        if self.health > 100:
            self.health = 100
        print("You fed your pet. Yummy!")

    def play(self):
        self.happiness += 15
        if self.happiness > 100:
            self.happiness = 100
        self.hunger += 5
        if self.hunger > 100:
            self.hunger = 100
        self.health -= 2
        if self.health < 0:
            self.health = 0
        print("You played with your pet. Woof woof!")

    def rest(self):
        self.health += 15
        if self.health > 100:
            self.health = 100
        self.hunger += 3
        if self.hunger > 100:
            self.hunger = 100
        print("Your pet took a rest. Zzzzz...")

    def display_status(self):
        print("\nCurrent pet status:")
        print(f"Hunger:    {self.get_status_bar(self.hunger)}")
        print(f"Happiness: {self.get_status_bar(self.happiness)}")
        print(f"Health:    {self.get_status_bar(self.health)}")

    def get_status_bar(self, value):
        """Returns a visual status bar"""
        bar_length = 20
        filled = int(round(value / 100 * bar_length))
        return '[' + '#' * filled + '-' * (bar_length - filled) + f'] {value}%'

    def show_dog(self):
        """Display different dog faces depending on the pet's status"""
        if self.happiness >= 70:
            dog_art = """
                             __
     ,                    ,"  e`--o      😊 Happy!
    ((                   (  | __,'
     \\~----------------' \_;/
     (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
"""
        elif self.hunger >= 50:
            dog_art = """
                             __
     ,                    ,"  T`--o      😫 Hungry...
    ((                   (  | __,'
     \\~----------------' \_;/
     (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
"""
        elif self.health <= 50:
            dog_art = """
                             __
     ,                    ,"  x`--o      😵 Sick!
    ((                   (  | __,'
     \\~----------------' \_;/
     (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
"""
        else:
            dog_art = """
                             __
     ,                    ,"  e`--o      😐 Normal
    ((                   (  | __,'
     \\~----------------' \_;/
     (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
"""
        print(dog_art)


def main():
    pet = VirtualPet()
    print("Welcome to Virtual Pet! Meet your dog:")
    pet.show_dog()

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Let your pet rest")
        print("4. Check pet's status")
        print("5. Quit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            pet.rest()
        elif choice == 4:
            pet.display_status()
        elif choice == 5:
            print("Goodbye! Take care of your virtual pet!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        pet.show_dog()  # Show the dog after every action

        # Ask if the user wants to continue
        while True:
            continue_choice = input("\nDo you want to continue? (y/n): ").lower()
            if continue_choice in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'.")

        if continue_choice == 'n':
            print("Goodbye! Take care of your virtual pet!")
            break


if __name__ == "__main__":
    main()
