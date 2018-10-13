_author_ = 'sbuono'

import sys

def resolve_case(line):
    X, R, C = line[0], line[1], line[2]
    if X > 6:
        return -1
    if R < X and C < X:
        return -1
    if (R * C) % X:
        return -1
    tmp = X / 2 + X % 2
    if C < tmp or R < tmp:
        return -1
    if X > 3 and (R * C) <= (X * 2):
        return -1
    if X > 4 and (R * C) <= (X * 3):
        return -1
    return 0

def main():
    file = sys.argv[1]
    with open(file, 'r') as f:
        tests = f.readline()
        i = 1
        for line in f:
            line = line.split()
            l = [int(x) for x in line]
            ret = resolve_case(l)
            print "Case #{}: {}".format(i, "RICHARD" if ret else "GABRIEL")
            i += 1
    return


if __name__ == '__main__':
    main()