from copy import deepcopy


def flip(current_pancakes, index):
    for i in range(index, index + flipper_size):
        if current_pancakes[i] == "-":
            current_pancakes[i] = "+"
        else:
            current_pancakes[i] = "-"


with open("/home/v2john/Downloads/A-large.in") as input_file:
    test_cases = int(input_file.readline())

    for test_case in range(test_cases):
        test_input_list = input_file.readline().split()

        init_pancakes = list(test_input_list[0])
        flipper_size = int(test_input_list[1])

        pancake_len = len(init_pancakes)
        current_pancakes = deepcopy(init_pancakes)
        flip_count = 0

        for i in range(pancake_len - flipper_size + 1):
            if current_pancakes[i] == '-':
                flip(current_pancakes, i)
                flip_count += 1

        if "-" in current_pancakes:
            print("Case #" + str(test_case + 1) + ": IMPOSSIBLE")
        else:
            print("Case #" + str(test_case + 1) + ": " + str(flip_count))
