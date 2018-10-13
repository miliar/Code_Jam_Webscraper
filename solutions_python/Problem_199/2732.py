#!/usr/bin/env python
import sys

def flip(pcake, fl, size):
    for i in range(fl, fl+size):
        if pcake[i] == "-":
            pcake[i] = "+"
        else:
            pcake[i] = "-"
    print pcake
    return pcake

def process(line):
    ln = line.split(" ")
    pcake = list(ln[0])
    size = int(ln[1])
    
    history = set()
    
    n = 0
    print pcake
    while "-" in pcake:
        for i in range(len(pcake)):
            if pcake[i] == "-":
                if i >= len(pcake)-size:
                    # boundaries
                    fl = len(pcake)-size
                else:
                    fl = i
                pcake = flip(pcake, fl, size)
                if "".join(pcake) in history:
                    return -1
                history.add("".join(pcake))
                n += 1
    return n

with open(sys.argv[2], "w") as fout:
    with open(sys.argv[1]) as fin:
        c = 0
        for line in fin:
            c += 1
            if c == 1:
                continue
            n = process(line[:-1])
            if n == -1:
                fout.write("Case #{}: IMPOSSIBLE\n".format(c-1))
            else:
                fout.write("Case #{}: ".format(c-1) + str(n) + "\n")
