#!/usr/bin/env python

import sys


def percent(n):
    if n % 25 == 0:
        fives = 1
    elif n % 5 == 0:
        fives = 5
    else:
        fives = 25

    if n % 4 == 0:
        twos = 1
    elif n % 2 == 0:
        twos = 2
    else:
        twos = 4

    return fives * twos


def freecell(bound, today, ever):
    if ever == 100:
        possible = (today == 100)
    elif ever == 0:
        possible = (today == 0)
    else:
        possible = (percent(today) <= bound)

    if possible:
        return "Possible"
    else:
        return "Broken"


def main():
    with open(sys.argv[1]) as file:
        file.readline()
        for n, line in enumerate(file):
            bound, today, ever = [int(s) for s in line.split()]
            print("Case #{0}: {1}".format(n + 1, freecell(bound, today, ever)))


main()
