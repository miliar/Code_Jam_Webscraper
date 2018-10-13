#!/usr/bin/env python


import fileinput
#from __future__ import print_function
import sys


def read_int():
    return int(input())


def read_ls():
    s = sys.stdin.readline()
    return [int(x) for x in s.split()]


def run():
    return 0


def main():
    # Read number of test cases
    for case in range(read_int()):
        # input data
        fields = sys.stdin.readline().split()

        shyness = [int(c) for c in fields[1]]
        # number of friends required
        nstanding=0
        nfriends=0
        for (s,c) in enumerate(shyness):
            # If the current shyness index is greater than the
            # current number of people standing, 
            if nstanding < s:
                # then invite enough friends to induce people to stand
                nfriends += s-nstanding
                nstanding += s-nstanding
            nstanding += c

        print("Case #{0:d}: {1:d}".format(case+1, nfriends))


if __name__ == "__main__":
    #profile.run('main()')
    sys.exit(main())

