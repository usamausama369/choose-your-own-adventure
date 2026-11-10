# A simple choose-your-own-adventure game.
# The player wakes up in a forest and chooses a path.

print("You wake up in a quiet forest. Sunlight filters through the trees.")
print("Ahead of you are three paths: left, right, and straight ahead.")

path = input("Which path do you take? ").lower()

# Each path leads to another choice.
if path == "left":
    print("\nYou find a small cottage with smoke rising from its chimney.")
    choice = input("Do you knock on the door or walk around back? ").lower()

    if choice == "knock":
        print("\nA friendly traveler opens the door and helps you find your way home.")
        print("You win!")
    else:
        print("\nYou wander into a muddy garden and get stuck until nightfall.")
        print("You lose!")

elif path == "right":
    print("\nYou come to a river. A wooden bridge crosses it, and a boat sits nearby.")
    choice = input("Do you cross the bridge or take the boat? ").lower()

    if choice == "bridge":
        print("\nThe bridge safely carries you to a sunny meadow. You find the way home.")
        print("You win!")
    else:
        print("\nThe boat springs a leak, and the current carries you far away.")
        print("You lose!")

elif path == "straight":
    print("\nYou discover a cave. You hear a gentle sound inside and birds outside.")
    choice = input("Do you enter the cave or follow the birds? ").lower()

    if choice == "birds":
        print("\nThe birds lead you to a village where people help you get home.")
        print("You win!")
    else:
        print("\nThe cave is dark, and you can't find your way back out.")
        print("You lose!")

else:
    # This runs if the player types something other than left, right, or straight.
    print("\nYou wait too long to choose, and the forest grows dark.")
    print("You lose!")
