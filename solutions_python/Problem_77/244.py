#!/usr/bin/env python

from sys import argv

def goro_sort(array):
    expected = sorted(array)
    in_position = 0

    for i,val in enumerate(array):
        if val == expected[i]:
            in_position = in_position + 1
    return float(len(array) - in_position)

if __name__ == "__main__":
    with open(argv[1], "r") as f:
        cases = int(f.readline())
        for i in range(cases):
            # Discard the array size line
            f.readline()
            array = [int(x) for x in f.readline().split()]
            print("Case #", i + 1, ": ", goro_sort(array), sep="")
