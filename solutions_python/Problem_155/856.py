#!/usr/bin/python

import sys


def ovation_iter(lst):
    guests = 0
    standing = 0
    for i in range(len(lst)):
        new_guests = 0
        if standing < i:
            new_guests = i - standing
        guests += new_guests
        standing += new_guests + int(lst[i])

    return guests

def run_it(filename):
    fh = open(filename, "r")
    lines = fh.readlines()[1:]
    ins = [l.split()[1] for l in lines]
    outs = ["Case #{}: {}".format(i+1, ovation_iter(inp)) for i, inp in enumerate(ins)]
    with open("out.txt", "w+") as outfh:
        outfh.write("\n".join(outs))


run_it(sys.argv[1])
