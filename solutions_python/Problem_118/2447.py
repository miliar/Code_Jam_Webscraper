# problems2.py
# @ismailsunni / antelope
from math import sqrt
def read_input(my_path):
    with open(my_path) as f:
        my_data = f.readlines()
    number_case = my_data[0]
    len_data = len(my_data)
    my_intervals = []
    for i in xrange(len_data - 1):
        # print my_data[i + 1]
        my_interval_list = my_data[i + 1].split(' ')
        if my_interval_list[1][-1] == '\n':
            my_interval_list[1] = my_interval_list[1][:-1]
        my_intervals.append(my_interval_list)
    return number_case, my_intervals

def is_palindrome(my_int):
    my_str = str(my_int)
    len_str = len(my_str)
    for i in range(len_str / 2):
        # print i
        if my_str[i] != my_str[len_str - 1 - i]:
            return False
    return True

def is_fair_square(my_int):
    if not is_palindrome(my_int):
        return False
    my_square_int = int(my_int) * int(my_int)
    my_square_str = str(my_square_int)
    if my_square_str[-1] == 'L':
        my_square_str = my_square_str[:-1]
    if is_palindrome(my_square_str):
        return True
    else:
        return False

def count_fair_square(A, B):
    new_A = int(sqrt(A))
    if new_A * new_A != A:
        new_A += 1
    new_B = int(sqrt(B))
    my_count = 0
    for i in xrange(new_B - new_A + 1):
        # print i + A, is_fair_square(i + A)
        if is_fair_square(i + new_A):
            my_count += 1
    return my_count

def write_result(my_results):
    my_text = ''
    for i in xrange(len(my_results)):
        my_text += 'Case #' + str(i + 1) + ': ' + str(my_results[i]) + '\n'
    print my_text
    f = open('output3', 'wt')
    f.write(my_text)
    f.close()

number_case, my_data = read_input('C-small-attempt0.in')
# print number_case
# print my_data
my_results = []
for my_d in my_data:
    my_result = count_fair_square(float(my_d[0]), float(my_d[1]))
    print my_result
    my_results.append(my_result)
write_result(my_results)