import sys

def calculate_minutes(pancake_list):

    max_pancakes = max(pancake_list)
    if max_pancakes == 1:
        return 1

    if max_pancakes == 2:
        return 2

    if max_pancakes == 3:
        return 3

    minutes = max_pancakes

    end = max_pancakes / 2 + 1
    for i in range(1, end):
        new_pancake_list = []
        special = 0
        for pancakes in pancake_list:
            if pancakes == max_pancakes:
                special = special + 1
                moved_pancakes = pancakes - i
                remaining_pancakes = pancakes - moved_pancakes
                new_pancake_list.append(remaining_pancakes)
                new_pancake_list.append(moved_pancakes)
            else:
                new_pancake_list.append(pancakes)
        minutes = min(minutes, special + calculate_minutes(new_pancake_list))

    return minutes

with open(sys.argv[1], 'r') as test_file:

    test_count = int(next(test_file))

    case_number = 1

    for test in range(test_count):

        diner_total = int(next(test_file))
        pancake_list = [int(s) for s in next(test_file).split()]

        print("Case #{}: {}".format(case_number, calculate_minutes(pancake_list)))

        case_number = case_number + 1
