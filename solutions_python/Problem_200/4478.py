#!/bin/python


def get_digit(number, index, digits):
    left = pow(10, digits - index -1 )
    number = number // left
    number = number % 10
    return number

def get_previous_number_to_check(number, num_len):
    if number < 10:
        return number
    to_change = None
    for i in range(num_len - 1):
        #print("i: "+ str(i))
        if get_digit(number, i, num_len) > get_digit(number, i+1, num_len):
            to_change = i
            change_to = get_digit(number, i, num_len) -1
            break

    num_str = list(str(number))
    num_str[to_change] = str(change_to)
    for i in range(to_change + 1, num_len):
        num_str[i] = '9'

    number = int("".join(num_str))
    return number


def is_tidy(num):
    if num < 10:
        return True
    num_len = len(str(num))
    for i in range(num_len - 1):
        if not (get_digit(num, i, num_len) <= get_digit(num, i+1, num_len) ):
            return False
    return True

# START
file = open("input.txt", 'r')
total_cases = int(file.readline())
out = open("output.txt", "w")
for i in range(total_cases):
    num_str = file.readline()
    num_str = num_str.replace("\r", "")
    num_str = num_str.replace("\n", "")
    num = int(num_str)
    num_len = len(num_str)
    temp = num
    #for temp in range(num, -1, -1):
    while temp != 0:
        if is_tidy(temp):
            out.write("Case #" + str(i+1) + ": " + str(temp)+ "\n")
            break
        temp = get_previous_number_to_check(temp, num_len)