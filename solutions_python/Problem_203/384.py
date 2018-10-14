#!/usr/bin/env python3
import sys


def main():
    input_file = sys.argv[1]
    solve(input_file)


def solve(input_file):
    with open(input_file) as f_in:
        t = int(next(f_in))
        for case in range(t):
            R, C = tuple(int(s) for s in next(f_in).split())
            cake = []
            for r in range(R):
                cake.append(list(next(f_in).rstrip()))
            cake_out, _ = solve_instance(C, cake)
            print("Case #%d:" % (case + 1))
            for r in cake_out:
                print(''.join(r))


def solve_instance(C, cake):
    cur = cake[0]
    haveline = False
    for i, r in enumerate(cake):
        if r == ['?' for _ in range(C)]: 
            if haveline:
                cake[i] = cur
            else:
                cakerest, line = solve_instance(C, cake[i+1:])
                cake[:(i+1)] = [line for _ in range(i+1)]
                cake[(i+1):] = cakerest
                haveline = True
                cur = line
        else:
            cake[i], _ = fill_line(r)
            haveline = True
            cur = cake[i]
    return cake, cake[0]


def fill_line(line):
    havechar = False
    cur = line[0]
    for i, c in enumerate(line):
        if c == '?':
            if havechar:
                line[i] = cur
            else:
                linerest, char = fill_line(line[(i + 1):])
                line[:(i+1)] = [char for _ in range(i+1)]
                line[(i+1):] = linerest
                havechar = True
                cur = char
        else:
            cur = c
            havechar = True
    return line, line[0]


if __name__ == '__main__':
    main()
