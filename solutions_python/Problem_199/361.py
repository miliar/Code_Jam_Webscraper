import os

HAPPY_SIDE = "+"
BLANK_SIDE = "-"
NO_SOLUTION = "IMPOSSIBLE"


def print_case(case_number, number_of_flips):
    if number_of_flips < 0:
        number_of_flips = NO_SOLUTION
    print("Case #" + str(case_number) + ": " + str(number_of_flips))


input_file = open("tests/A-large.in", "r")
number_of_testcases = int(input_file.readline())
for case_number in range(1, number_of_testcases + 1):
    pancakes, pancake_flipper_size = input_file.readline().split(" ")
    pancakes = list(pancakes)
    pancake_flipper_size = int(pancake_flipper_size)
    number_of_pancakes = len(pancakes)

    number_of_flips = 0

    for pancake_index in range(0, number_of_pancakes):
        if pancakes[pancake_index] == HAPPY_SIDE:
            # No need to flip
            continue
        if pancakes[pancake_index] == BLANK_SIDE:
            # We need to flip it
            if pancake_index + pancake_flipper_size > number_of_pancakes:
                # Pancake flipper is out of bounds, unsolvable.
                number_of_flips = -1
                break
            # Flip the pancakes
            number_of_flips += 1
            for pancake_index_2 in range(pancake_index, pancake_index + pancake_flipper_size):
                if pancakes[pancake_index_2] == BLANK_SIDE:
                    pancakes[pancake_index_2] = HAPPY_SIDE
                elif pancakes[pancake_index_2] == HAPPY_SIDE:
                    pancakes[pancake_index_2] = BLANK_SIDE

    # Print the number of flips it took
    print_case(case_number, number_of_flips)
