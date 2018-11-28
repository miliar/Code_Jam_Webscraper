# problem1.py
# @ismailsunni / antelope
def check_result_array(my_str):
    if '.' in my_str:
        return '.'  # Unfinished
    number_T = my_str.count('T')
    if number_T > 1:
        return None  # Draw
    my_str = my_str.replace('T', '')
    if 'O' in my_str and 'X' in my_str:
        return None # Draw
    else:
        return my_str[0]  # X or O

def check_result_case(my_case):
    is_unfinished = 0
    len_case = len(my_case)
    # check horizontal
    for i in range(len_case):
        my_result = check_result_array(my_case[i])
        if my_result == 'X':
            return 'X'
        if my_result == 'O':
            return 'O'
        if my_result == '.':
            is_unfinished = True
    # check vertical and diagonal
    # create vertical arrays
    my_extra_arrays = []
    for i in range(len_case):
        my_array = ''
        for j in range(len_case):
            my_array += my_case[j][i]
        my_extra_arrays.append(my_array)
    # create diagonal arrays
    my_diagonal_array1 = ''
    my_diagonal_array2 = ''
    for i in range(len_case):
        my_diagonal_array1 += my_case[i][i]
        my_diagonal_array2 += my_case[len_case - i - 1][i]
    my_extra_arrays.append(my_diagonal_array1)
    my_extra_arrays.append(my_diagonal_array2)
    for i in range(len(my_extra_arrays)):
        my_result = check_result_array(my_extra_arrays[i])
        if my_result == 'X':
            return 'X'
        if my_result == 'O':
            return 'O'
    if is_unfinished:
        return 'U'  # Unfinished
    else:
        return 'D'  # Draw

def write_result(my_results):
    text = ''
    my_counter = 1
    for my_result in my_results:
        if my_result == 'X':
            text += 'Case #' + str(my_counter) + ': X won\n'
        elif my_result == 'O':
            text += 'Case #' + str(my_counter) + ': O won\n'
        elif my_result == 'D':
            text += 'Case #' + str(my_counter) + ': Draw\n'
        elif my_result == 'U':
            text += 'Case #' + str(my_counter) + ': Game has not completed\n'
        my_counter += 1
    print text
    f = open('output', 'wt')
    f.write(text)
    f.close()

with open('A-large.in') as f:
    my_data = f.readlines()
number_case = int(my_data[0])
print 'number_case', number_case
list_case = []
my_results = ''
for i in range(number_case):
    # add to list_case
    my_case = []
    my_case.append(my_data[i * 5 + 1][:-1])
    my_case.append(my_data[i * 5 + 2][:-1])
    my_case.append(my_data[i * 5 + 3][:-1])
    my_case.append(my_data[i * 5 + 4][:-1])
    my_result = check_result_case(my_case)
    my_results += my_result
    print i + 1, 'Result : ', check_result_case(my_case)
write_result(my_results)
