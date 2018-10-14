#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


import sys


def tidy(x):
    c = 0
    x = list(x)
    while sorted(x) != x:
        if x[c] > x[c+1]:
            x[c] = str(int(x[c])-1)
            x[c+1::] = "9"*len(x[c+1::])
        else:
            c += 1
        if c+1 == len(x):
            x[c] = str(int(x[c]))
            x[c+1::] = "9"*len(x[c+1::])
            c = 0
            continue
    while x[0] == "0":
        x = x[1::]
    x = "".join(x)
    return(x)


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        with open(filename.replace(".in", ".out"), "w") as f2:
            for i, line in enumerate(f.readlines()):
                if i != 0:
                    f2.write("Case #{}: {}\n".format(i, tidy((line.strip()))))
