#! /usr/bin/python
# GCJ 2011 QR - Bot Trust

from sys import stdin


def parse_bot_instructions(line) :
    tokens = line.strip().split(' ')

    instructions = []
    for (color, pos) in zip(tokens[1::2], tokens[2::2]) :
        instructions.append((color, int(pos)))

    return instructions


def count_min_steps(instructions) :
    orange_steps, blue_steps = 0, 0
    orange_pos, blue_pos = 1, 1

    for (color, pos) in instructions :
        if color == 'O' :
            orange_steps += abs(pos - orange_pos) + 1
            orange_pos = pos
            if orange_steps <= blue_steps :
                orange_steps = blue_steps + 1
        elif color == 'B' :
            blue_steps += abs(pos - blue_pos) + 1
            blue_pos = pos
            if blue_steps <= orange_steps :
                blue_steps = orange_steps + 1

    return max(orange_steps, blue_steps)


def main() :
    input_data = stdin.readlines()

    n_tests = int(input_data[0])
    for i in range(1, n_tests + 1) :
        instructions = parse_bot_instructions(input_data[i])
        solution = count_min_steps(instructions)
        print('Case #{0}: {1}'.format(i, solution))

if __name__ == '__main__' :
    main()
