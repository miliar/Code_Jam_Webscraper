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
            result = flip_pancakes(case_input)

            output_file.write('Case #' + str(case_number) + ": " + result + '\n')


def flip_pancakes(case_input):
    pancakes = case_input.split(' ')[0]
    flipper_size = int(case_input.split(' ')[1])

    flip_count = 0

    for i in range(0, len(pancakes) - flipper_size + 1):
        if pancakes[i] == '-':
            pancakes = flip(pancakes, flipper_size, i)
            flip_count += 1

    if '-' in pancakes:
        return 'IMPOSSIBLE'

    return str(flip_count)

def flip(pancakes, size, start):
    return pancakes[0:start] + pancakes[start:start + size].replace('-', 't').replace('+', '-').replace('t', '+') + pancakes[start + size:]

if __name__ == '__main__':
    main()
