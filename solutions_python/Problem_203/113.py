#!/usr/bin/env python3

def fill(cake):
    cur_line = []
    last_line = cur_line
    for i,row in enumerate(cake):
        empty = True
        occ = 0
        for j,letter in enumerate(row):
            occ += 1
            if letter != "?":
                empty = False
                cur_line.extend([letter]*occ)
                occ = 0
        if not empty:
            cur_line.extend([cur_line[-1]]*occ)
            cake[i] = cur_line
            last_line = cur_line
            cur_line = []
        else:
            cake[i] = last_line


def show(cake):
    for row in cake:
        print(''.join(row))


import sys
file=sys.stdin

n = int(file.readline()) # number of cases
for i in range(1, n+1):
    R, C = map(int, file.readline().split())
    cake = []
    for r in range(R):
        cake.append(list(file.readline()[:C]))

    fill(cake)

    print("Case #%d:" % (i))
    show(cake)
