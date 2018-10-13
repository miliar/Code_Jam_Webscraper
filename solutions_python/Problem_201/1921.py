import re

def bathroom_stalls(filename):
    txt_file = open(filename, 'r')
    txt_file_result = open('C-small1-result.txt', 'w')
    test_cases_amount = int(txt_file.readline().rstrip('\n'))

    for x in range(1, test_cases_amount + 1):
        test_info = txt_file.readline().rstrip('\n').split()
        actual_stalls_amount = int(test_info[0])
        actual_people_amount = int(test_info[1])

        test_result = solve(actual_people_amount, actual_stalls_amount)

        txt_file_result.write('Case #' + str(x) + ': ' + str(test_result[0]) + ' ' + str(test_result[1]) + '\n')

    txt_file_result.close
    txt_file.close

def solve(people_remaining, stalls_amount):

    empty_slots = [stalls_amount]

    while (people_remaining > 0):

        biggest_space = max(empty_slots)
        max_diff = int(biggest_space/2)
        min_diff = int(biggest_space/2) if biggest_space%2 != 0 else int(biggest_space/2) - 1 
        empty_slots.append(max_diff)
        empty_slots.append(min_diff)

        empty_slots.pop(empty_slots.index(biggest_space))
        people_remaining -= 1

    return [max_diff, min_diff]

bathroom_stalls('C-small-1-attempt0.in')