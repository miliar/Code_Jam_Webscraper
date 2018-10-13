#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def ominous_omino(path):
    
    with open(path) as f:
        content = f.readlines()
    t = int(content[0].replace("\n", ""))
    for i in range(1, t+1):
        line = content[i].replace("\n", "").split(" ")
        x = int(line[0])
        r = int(line[1])
        c = int(line[2])

        if x >= 7:  # can choose a xomino with a "hole" in it
            print("Case #{}: RICHARD".format(i))
            continue
        if ((r*c) % x) != 0 or r*c == 0:  # the grid cannot be filled by xominoes
            print("Case #{}: RICHARD".format(i))
            continue
        if r < x and c < x:  # can choose a piece that do not fit
            print("Case #{}: RICHARD".format(i))
            continue
        if x <= 2:
            print("Case #{}: GABRIEL".format(i))
            continue
        if (x % 2 == 1 and min(r, c) <= x//2) or (x % 2 == 0 and min(r, c) < x//2):  # can choose a piece that do not fit
            print("Case #{}: RICHARD".format(i))
            continue            

        if x <= 3:  # simple cases
            print("Case #{}: GABRIEL".format(i))
            continue
        if x == 4 and r*c >= 12:
            print("Case #{}: GABRIEL".format(i))
            continue
        if x == 4:
            print("Case #{}: RICHARD".format(i))
            continue


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <path_to_input_file>")
    else:
        ominous_omino(sys.argv[1])
