import sys
import numpy as np


def read_case(line):
    return int(line.strip())

def is_tidy(number):
    number = [int(x) for x in str(number)]
    for i in range(1, len(number)):
        if number[i] < number[i-1]:
            return False
    return True


def make_solution(max_number):
    for i in range(max_number, 0, -1):
        if is_tidy(i):
            return i

if __name__ == "__main__":
    f = sys.stdin
    # f = open("samples.text")
    count = int(f.readline())
    for c in range(count):
        case_c = read_case(f.readline())
        solution = make_solution(case_c)
        print("Case #{}: {}".format(c+1, solution))