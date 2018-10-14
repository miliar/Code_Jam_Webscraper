#! /usr/bin/env python
# welcome.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2009 Sep 


import sys

PATTERN = "welcome to code jam"
PATTERN_LEN = len(PATTERN)

def zeros(x_size, y_size):
    return [[0 for i in range(y_size)] for b in range(x_size)]

def count_welcomes(line):
    # empty array
    line_len = len(line)
    a = zeros(PATTERN_LEN, line_len)
    for i in range(PATTERN_LEN - 1, -1, -1):
        for j in range(line_len - 1, -1, -1):
            if PATTERN[i] == line[j]:
                if (j + 1) == line_len:
                    a[i][j] += 1
                else:
                    if (i + 1) != PATTERN_LEN:
                        a[i][j] += a[i+1][j+1] % 10000
                    else:
                        a[i][j] += 1
            if (j + 1) != line_len:
                a[i][j] += a[i][j+1] % 10000
    return a[0][0] % 10000


def main():
    file = open(sys.argv[1])
    # eat first line
    nb_cases = int(file.readline())
    case_nb = 1
    for line in file:
        print "Case #%d: %04d" % (case_nb, count_welcomes(line))
        case_nb += 1
    file.close()

if __name__ == "__main__":
    main()
