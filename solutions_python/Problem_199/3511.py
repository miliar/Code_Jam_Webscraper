# open_file = open('A-small-attempt2.in')
open_file = open('Pancakes.in')

test_cases = int(open_file.readline())
case_list = []
for line in open_file:
    case_list.append(line.rstrip('\n'))

# for element in case_list:
#     print(element)

# Will flip a subsequence of pancakes of length k at index cake_index.
def flip(line_of_cakes, cake_index, k, flip_counter):
    end_flip = cake_index + k
    for hotcake in line_of_cakes[cake_index:end_flip]:
        if hotcake == '-':
            line_of_cakes[cake_index] = '+'
        elif hotcake == '+':
            line_of_cakes[cake_index] = '-'
        cake_index += 1
    flip_counter += 1
    return flip_counter


HAPPY = '+'
case_number = 0
# For each case:
for case in case_list:
    # CASE --> list
    case_number += 1
    temp = case.split()
    pan_width = int(temp[1])
    cake_line = list(case[:-2])
    flip_count = 0
    # print(cake_line)
    for pancake in range(len(cake_line) - pan_width + 1):
            if cake_line[pancake] is not HAPPY:
                flip_count = flip(cake_line, pancake, pan_width, flip_count)
    # print(cake_line)

    # Check the line of pancakes for '-'
    if '-' in cake_line:
        outcome = 'IMPOSSIBLE'
    else:
        outcome = flip_count
    print('Case #{}: {}'.format(case_number, outcome))