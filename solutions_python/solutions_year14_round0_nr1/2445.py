#!/usr/bin/env python3
# coding=utf-8

"""
GCJ 2014: Qualification round, problem A

Author: A. Ayala
"""
import sys

def its_magic(fd):
    """
    Read a cse from the file and return the answer
    """
    # First number: Anwser 1
    # If the user cheats saying an invalid number rows[s] will be the empty set
    rows = [set(), set()]
    for s in range(2):
        u = int(fd.readline().strip())
        for k in range(4):
            txt = fd.readline()
            if k == u-1:
                rows[s] = set(txt.strip().split())

    # Now check the intersection of both rows
    res = rows[0] & rows[1]
    if len(res) == 0:
        return "Volunteer cheated!"
    elif len(res) == 1:
        return res.pop()
    else:
        return "Bad magician!"


def solve(fd):
    """
    Solve all the cases from fd
    """

    t = int(fd.readline().strip())
    for k in range(t):
        res = its_magic(fd)
        print("Case #{}: {}".format(k+1, res))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        infile = sys.stdin
    else:
        infile = open(sys.argv[1], 'r')

    solve(infile)

    infile.close()
