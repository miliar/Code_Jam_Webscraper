#!/usr/bin/python3

import sys


def main():
    with open(sys.argv[1]) as input_file:
        content = [line.strip('\n') for line in input_file.readlines()]

    case_count = int(content[0])

    with open('output', 'w') as output_file:
        for case_number in range(1, case_count + 1):
            case_input = content[case_number]

            # Do computations here
            result = str(last_tidy(int(case_input)))

            output_file.write('Case #' + str(case_number) + ": " + result + '\n')


def last_tidy(N):
    i = 0
    Nstr = str(N)[::-1]
    while pow(10, i + 1) <= N:
        if Nstr[i] < Nstr[i + 1]:
            N -= N % pow(10, i + 1) + 1
            Nstr = str(N)[::-1]
        i += 1
    return N


if __name__ == '__main__':
    main()
