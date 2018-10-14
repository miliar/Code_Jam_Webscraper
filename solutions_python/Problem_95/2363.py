#!/usr/bin/env python

from __future__ import with_statement

dict = {
    "a": "y",
    "c": "e",
    "b": "h",
    "e": "o",
    "d": "s",
    "g": "v",
    "f": "c",
    "i": "d",
    "h": "x",
    "k": "i",
    "j": "u",
    "m": "l",
    "l": "g",
    "o": "k",
    "n": "b",
    "q": "z",
    "p": "r",
    "s": "n",
    "r": "t",
    "u": "j",
    "t": "w",
    "w": "f",
    "v": "p",
    "y": "a",
    "x": "m",
    "z": "q",
    " ": " ",
}

def translate(line):
    result = ""

    for c in line:
        result += dict[c]

    return result

def main(argv):
    if len(argv) == 2:

        goolines = []
        with open(argv[1]) as f:
            for line in f.readlines():
                goolines.append(line[:-1])

        T = int(goolines[0])

        if not len(goolines[1:]) == T:
            raise "Wrong number of lines of input."

        goolines = goolines[1:]

        i = 1
        for line in goolines:
            print "Case #%s: %s" % (i, translate(line))
            i += 1

    else:
        print "Usage: ./problem_a.py input.txt"

if __name__ == '__main__':
    from sys import argv
    main(argv)








