#!/usr/bin/python
from sys import argv

def solve(case):
    first_half, second_half = case[0:5], case[5:10]

    first_answer = int(first_half[0])
    row1 = set(first_half[first_answer].split())

    second_answer = int(second_half[0])
    row2 = set(second_half[second_answer].split())

    return row1.intersection(row2)


def main():
    with open(argv[1], "r") as f:
        T = int(f.readline())
        lines = f.readlines()

    start = 0
    increment = 10

    for case_number in xrange(1, T+1):
        stop = start + increment
        case = lines[start:stop]

        result = solve(case)
        
        if len(result) == 1:
            print("Case #{0}: {1}".format(case_number, result.pop()))
        elif len(result) == 0:
            print("Case #{0}: Volunteer cheated!".format(case_number))
        else:
            print("Case #{0}: Bad magician!".format(case_number))

        start += increment

if __name__ == '__main__':
    main()