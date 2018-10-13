# -*- coding: utf-8 -*-
__author__ = "Sommily"

input = """4
132
1000
7
111111111111111110
"""


def read_input():
    f = open("/Users/Sommily/Downloads/B-small-attempt0.in", 'r')
    lines = f.readlines()
    f.close()
    input = "".join(lines)
    return input


def check(number):
    number_str = str(number)
    last_n = None
    for n in number_str:
        if last_n is None:
            last_n = n
            continue

        if int(last_n) > int(n):
            return False
        last_n = n

    return True


def calc(number):
    number = int(number) - 1
    return number


def calc_v2(number):
    new_number = None
    for i, n in enumerate(str(number)):
        if new_number is None:
            new_number = n
            continue

        if int(new_number[-1]) > int(n):
            new_number += str(int(n) - 1)
            new_number += str(number)[i:]
            return new_number

    return new_number


if __name__ == "__main__":
    input = read_input()
    case_count = input.split('\n')[0]
    i = 0
    for case_data in input.split('\n')[1:]:
        i += 1
        if check(case_data):
            print("Case #{}: {}".format(i, case_data))
        else:
            new_case_data = calc(case_data)
            while not check(new_case_data):
                new_case_data = calc(new_case_data)
                # print("calc: " + case_data)
            print("Case #{}: {}".format(i, new_case_data))
