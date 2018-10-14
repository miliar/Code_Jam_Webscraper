#!/usr/bin/env python

import sys

infile = sys.stdin
str = 'welcome to code jam'

N = int(infile.readline().strip())

for case in range(1, N + 1):
    line = infile.readline().strip()
    table = [[0 for i in range(len(line) + 1)] for j in range(len(str) + 1)]
    table[0] = [1 for i in range(len(line) + 1)]

    # print('%s: %s' % (' ', table[0]))

    for i in range(1, len(str) + 1):
        for j in range(1, len(line) + 1):
            table[i][j] = table[i][j - 1]
            if line[j - 1] == str[i - 1]:
                table[i][j] += table[i - 1][j]
                if table[i][j] >= 10000:
                    table[i][j] -= 10000
        # print('%s: %s' % (str[i - 1], table[i]))
                
    print('Case #%d: %.4d' % (case, table[len(str)][len(line)]))
