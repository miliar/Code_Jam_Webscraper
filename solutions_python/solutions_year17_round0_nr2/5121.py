#!/usr/bin/env python3

def get_cases():
    with open('B-small-attempt0.in') as f:
        for line in f:
            yield line

def solve(line):
    n = int(line)
    for i in range(n, 0, -1):
        last_max = 0
        str_number = str(i)
        for nb, c in enumerate(str_number):
            current = int(c)
            if max(current, last_max) != current:
                break
            last_max = current
            if nb+1 == len(str_number):
                return i
    return -1


if __name__ == '__main__':
    for nb, line in enumerate(get_cases()):
        if nb == 0:
            nb_cases = line
        else:
            result = solve(line)
            print("Case #{}: {}".format(nb, result))
