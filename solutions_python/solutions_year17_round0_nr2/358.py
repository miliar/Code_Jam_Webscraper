# pylint: disable=missing-docstring
import sys


def problem(case):
    """
    othercase = int(case)
    sol = 0
    for i in range(othercase + 1):
        test = [int(x) for x in str(i)]
        allowed = 0
        check = True
        for j in test:
            if j < allowed:
                check = False
            allowed = j
        if check:
            sol = i
    """

    case = [int(x) for x in case]
    allowed = 9
    for i in range(len(case) - 1, -1, -1):
        if case[i] < allowed:
            allowed = case[i]
        if case[i] > allowed:
            for j in range(i+1, len(case)):
                case[j] = 9
            case[i] -= 1
            allowed = case[i]
    result = int("".join([str(x) for x in case]))
    #assert sol == result, f"{sol} != {result} for {othercase}"
    return result

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
