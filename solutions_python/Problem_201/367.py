import math
import os


def print_case(case_number, max, min):
    print("Case #" + str(case_number) + ": " + str(max) + " " + str(min))


def solve_problem(num_stalls, num_people):
    if num_people == 1:
        if num_stalls % 2 == 0:
            return [num_stalls // 2 - 1, num_stalls // 2 - 2]
        else:
            return [num_stalls // 2 - 1, num_stalls // 2 - 1]
    if num_stalls == 3 and num_people >= 1:
        return [0, 0]
    if num_stalls % 2 == 1:
        # If the number of stalls will split in to two even sections, reduce
        # the problem by half
        return solve_problem((num_stalls + 1) // 2, num_people // 2)
    if num_stalls % 2 == 0:
        # The problem can split in to two different sizes
        if num_people % 2 == 0:
            # place a person in the middle and use the larger half
            return solve_problem(num_stalls // 2 + 1, num_people // 2)
        else:
            # place a person in the middle and use the smaller half
            return solve_problem(num_stalls // 2, num_people // 2)


input_file = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "tests/C-large.in"), "r")
number_of_cases = int(input_file.readline())
for case_number in range(1, number_of_cases + 1):
    num_stalls, num_people = input_file.readline().split()
    num_stalls = int(num_stalls)
    num_people = int(num_people)

    maximum, minimum = solve_problem(num_stalls + 2, num_people)
    print_case(case_number, maximum, minimum)
