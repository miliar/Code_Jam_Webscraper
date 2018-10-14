import numpy as np
import sys
sys.setrecursionlimit(100000)

def is_tidy(digits):
    return digits == sorted(digits)

def nearest_smaller_tidy(digits):
    if digits == [0]:
        return [0]
    if not is_tidy(digits):
        front_digits = digits[:-1]
        front_digits[-1] -= 1

        front = nearest_smaller_tidy(front_digits)
        return front + [9]
    else:
        return digits

f = open('B-large.in', 'r')
output = open("out.txt", 'w+')

first_line = f.readline()
for index, line in enumerate(f):
    line = line.strip()
    line = [int(i) for i in line]

    digits = nearest_smaller_tidy(line)
    digits.reverse()
    answer = 0
    for power, digit in enumerate(digits):
        answer += digit * (10 ** power)

    string = "Case #" + str(index+1) + ": " + str(answer)
    output.write(string + "\n")

f.close()
output.close()