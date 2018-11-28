#!/usr/bin/env python

DEBUG = False

def read_stdin_lines():
    import fileinput
    return [line for line in fileinput.input()]

def parse_lines(lines):
    lines.pop(0)
    return [map(int, line.split()) for line in lines]

def solve(i):
    assert(len(i) == 3)
    X, R, C = i
    if X > 6:
        if DEBUG:
            return "X > 6"
        return "RICHARD"
    if (R * C) % X != 0:
        if DEBUG:
            return "(R * C) % X != 0"
        return "RICHARD"
    if R + C < X:
        if DEBUG:
            return 'R + C < X'
        return "RICHARD"
    if R < (X+1)/2 or C < (X+1)/2:
        if DEBUG:
            return 'R < X+1/2 or C < X+1/2'
        return "RICHARD"
    if R < X and C < X:
        if DEBUG:
            return 'R < X and C < X'
        return "RICHARD"
    if X >= 4 and min(R, C) <= X/2:
        if DEBUG:
            return 'X >= 4 and min(R, C) <= X/2'
        return "RICHARD"
    return "GABRIEL"

def print_outputs(outputs):
    for n, output in enumerate(outputs):
        print "Case #{}: {}".format(n+1, output)

if __name__ == '__main__':
    lines = read_stdin_lines()
    inputs = parse_lines(lines)
    outputs = map(solve, inputs)
    print_outputs(outputs)
