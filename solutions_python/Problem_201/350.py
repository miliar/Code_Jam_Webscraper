# pylint: disable=missing-docstring
import sys
from collections import deque


def problem(case):
    stalls, people = [int(x) for x in case.split(" ")]
    data = deque([[stalls, 1]])
    while True:
        size, occs = data.popleft()
        size -= 1
        a = size // 2
        b = size // 2 + (size % 2)
        if len(data) != 0 and data[-1][0] == b:
            data[-1][1] += occs
        else:
            data.append([b, occs])
        if data[-1][0] == a:
            data[-1][1] += occs
        else:
            data.append([a, occs])
        people -= occs
        if people <= 0:
            return f"{b} {a}"



def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            case = nextline(infile)
            result += 'Case #{}: {}\n'.format(1 + run, problem(case))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()
