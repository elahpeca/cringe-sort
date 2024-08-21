import random
import time

def cringe_sort(input_list):
    """
    Cringe sort: Randomly shuffles the list until it is sorted.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, (int, float)) for x in input_list):
        raise TypeError("List elements must be numbers.")
    attempt_count = 0
    while True:
        attempt_count += 1
        # Shuffle the list elements
        shuffled_list = random.sample(input_list, len(input_list))
        # Check if the list is sorted
        if all(shuffled_list[i] <= shuffled_list[i + 1] for i in range(len(shuffled_list) - 1)):
            return shuffled_list
        else:
            print(f"Attempt #{attempt_count}: {shuffled_list}")
            time.sleep(0.5) # Pause for a bit of dramatic effect

def get_user_input():
    """
    Gets user input for the list, validating it and providing feedback.
    """
    while True:
        input_str = input("Enter numbers separated by spaces (or type 'exit' to quit): ")
        if input_str.lower() == 'exit':
            return None
        try:
            my_list = [float(x) for x in input_str.split()]
            return my_list
        except ValueError:
            print("Oops! Please enter numbers only. Try again. 🤓")

if __name__ == "__main__":
    print("Welcome to the Cringe Sort Experience! 🤪")
    print("Prepare for a wild ride of random shuffles until...")
    print("...the list magically sorts itself (hopefully). 🤞")

    while True:
        my_list = get_user_input()
        if my_list is None:
            break # User chose to exit

        # Perform cringe sort
        sorted_list = cringe_sort(my_list)
        print(f"\nSuccess! The list is finally sorted (after many, many tries): {sorted_list}")
        print("It was a close call, but we did it! 🥳")
        print("----------------------------------------------------") # Separator between attempts

    print("Thanks for using Cringe Sort! ❤️")