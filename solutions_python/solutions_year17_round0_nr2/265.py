from itertools import count

def is_tidy(number_as_int_list):
    must_be_greater_than_or_equal_to = 0
    for next_digit in number_as_int_list:
        if next_digit < must_be_greater_than_or_equal_to:
            return False
        must_be_greater_than_or_equal_to = next_digit
    return True

def flip_digit(number_as_int_list, at):
    i = len(number_as_int_list) - at - 1
    number_as_int_list[i] = 9
    number_as_int_list[i - 1] -= 1
    return number_as_int_list


def case(n):
    at_digit = 0
    while not is_tidy(n):
        n = flip_digit(n, at_digit)
        at_digit += 1
    return n

def cases(data):
    lines = int(data[0])
    for case_number, line in zip(count(1), data[1:]):
        result = case([int(c) for c in line.strip()])
        while result[0] == 0:
            result.pop(0)
        output = ''.join([ str(d) for d in result ])
        print("Case #{}: {}".format(case_number, output))

with open('input', 'r') as f:
    cases(f.readlines())
