def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    
    choice = input("What do you want to do? (Enter 1 or 2): ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def left_path():
    print("\nYou take the left path and encounter a river.")
    print("1. Try to swim across.")
    print("2. Look for a bridge.")
    
    choice = input("What do you want to do? (Enter 1 or 2): ")
    
    if choice == "1":
        print("\nYou try to swim across but the current is too strong. You are swept away. Game over!")
    elif choice == "2":
        print("\nYou find a bridge and safely cross the river. You win!")
    else:
        print("Invalid choice. Please try again.")
        left_path()

def right_path():
    print("\nYou take the right path and encounter a wild bear.")
    print("1. Try to fight the bear.")
    print("2. Run away.")
    
    choice = input("What do you want to do? (Enter 1 or 2): ")
    
    if choice == "1":
        print("\nYou try to fight the bear but it overpowers you. Game over!")
    elif choice == "2":
        print("\nYou run away and find a safe place to hide. You win!")
    else:
        print("Invalid choice. Please try again.")
        right_path()

# Start the game
start_game()