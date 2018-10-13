#!/usr/bin/python

import sys


def main():
    T = next(sys.stdin)
    for case, line in enumerate(sys.stdin, 1):
        smax, s = line.split()
        standing = 0
        extra = 0
        for shyness, people in enumerate(s):
#            print shyness, people, "->",
            people = int(people)
            if shyness > standing:
                extra += shyness - standing
                standing += shyness - standing
            standing += people
#            print standing, extra
        print "Case #{}: {}".format(case, extra)


main()

