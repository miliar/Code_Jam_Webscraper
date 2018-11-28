import re

def string_to_list_of_ints(string):
    list_of_strings = re.split("\s", string)
    list_of_ints = map(int, list_of_strings)
    return list_of_ints

input = open("input.txt", 'r')

num_of_test_cases = int(input.readline()[:-1])

for i in range(1,num_of_test_cases + 1):
    first_guess = int(input.readline()[:-1])
    row1_1 = string_to_list_of_ints(input.readline()[:-1])
    row2_1 = string_to_list_of_ints(input.readline()[:-1])
    row3_1 = string_to_list_of_ints(input.readline()[:-1])
    row4_1 = string_to_list_of_ints(input.readline()[:-1])
    square_1 = [row1_1, row2_1, row3_1, row4_1]

    second_guess = int(input.readline()[:-1])
    row1_2 = string_to_list_of_ints(input.readline()[:-1])
    row2_2 = string_to_list_of_ints(input.readline()[:-1])
    row3_2 = string_to_list_of_ints(input.readline()[:-1])
    row4_2 = string_to_list_of_ints(input.readline()[:-1])
    square_2 = [row1_2, row2_2, row3_2, row4_2]

    chosen_row_1 = square_1[first_guess-1]
    chosen_row_2 = square_2[second_guess-1]

    if len(set(chosen_row_1).intersection(set(chosen_row_2))) > 1:
        print "Case #" + str(i) + ": Bad magician!"
    elif len(set(chosen_row_1).intersection(set(chosen_row_2))) < 1:
        print "Case #" + str(i) + ": Volunteer cheated!"
    else:
        for num in chosen_row_1:
            if num in chosen_row_2:
                print "Case #" + str(i) + ": " + str(num)
