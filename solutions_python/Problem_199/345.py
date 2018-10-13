# pylint: disable=missing-docstring
import sys


def problem(case):
    pancakes, size = case.split(" ")
    size = int(size)
    data = [x == "+" for x in pancakes]
    counter = 0
    for i in range(len(data) - size + 1):
        if not data[i]:
            for j in range(size):
                data[i + j] = not data[i + j]
            counter += 1
    if all(data):
        return counter
    return "IMPOSSIBLE"



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
