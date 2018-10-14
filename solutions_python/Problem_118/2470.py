# -*- coding: utf-8 -*-
import math


def open_files():
    f = open('C-small-attempt0.in', 'r')
    g = open('output.out', 'w')
    return f, g


def count_squares(root_list):
    answer = 0
    for root in root_list:
        if is_palindrome(root * root):
            answer += 1
    return answer


def is_palindrome(integer):
    number = str(integer)
    if len(number) < 2:
        return True
    if number[0] == number[len(number) - 1]:
        return is_palindrome(number[1:len(number) - 1])


def list_roots(minimum, maximum):
    root_list = []
    min_root = int(math.ceil(math.sqrt(minimum)))
    max_root = int(math.ceil(math.sqrt(maximum + 1)))
    for integer in range(max_root - min_root):
        if is_palindrome(integer + min_root):
            root_list.append(integer + min_root)
    return root_list


f, g = open_files()

number_of_test_cases = int(f.readline())

for index in range(number_of_test_cases):
    interval = f.readline().split()
    minimum = int(interval[0])
    maximum = int(interval[1])
    eligible_roots = list_roots(minimum, maximum)
    answer = str(count_squares(eligible_roots))
    print "Case #" + str(index + 1) + ": " + answer
    g.write("Case #" + str(index + 1) + ": " + answer + '\n')
