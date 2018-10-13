#!/usr/bin/env python
import sys

i = 0
t = 0
c = 0
n = 0
m = 0
x = 0
lawn = []

def calculate():
    global n, m, lawn

    clear_row = set()
    impossible_row = set()
    for i, row in enumerate(lawn):
        if row.count(2) == 0:
            clear_row.add(i)
        elif row.count(1) > 0:
            impossible_row.add(i)

    clear_col = set()
    for row in impossible_row:
        for j, col in enumerate(lawn[row]):
            if col == 1 and j not in clear_col:
                if [lawn[z][j] for z in range(n)].count(2) == 0:
                    clear_col.add(j)
                else:
                    return 'NO'
    return 'YES'

def process(line):
    global t
    global i
    global c
    global n
    global m
    global x
    global lawn

    i += 1;

    if i == 1:
        t = int(line)
        c = 1
        n = 0
    else:
        if n == 0:
            (n, m) = [int(d) for d in line.split()]
            x = 0
        else:
            lawn.append([int(d) for d in line.split()])
            x += 1

        if x > 0 and x == n:
            result = calculate()
            print "Case #{}: {}".format(c, result)
            c += 1
            n = 0
            m = 0
            lawn = []



if len(sys.argv) < 2:
    print "Please supply the input file as argument"
    sys.exit(2)

filename = sys.argv[1]
with open(filename) as f:
    for line in f:
        if len(line.strip()):
            process(line.strip())
