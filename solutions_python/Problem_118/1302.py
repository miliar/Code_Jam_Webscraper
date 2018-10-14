#!/usr/bin/env python2
# by Santiago Saavedra

from math import sqrt, floor, ceil

def is_palindrome(x):
    if type(x) is not int:
        if ceil(x) != floor(x):
            return False
        x = int(x)
    s = str(x)
    for i in xrange(len(s) / 2 + 1):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def parse_case(case):
    a, b = case.split()
    a, b = int(a), int(b)

    found = 0
    for n in xrange(a, b + 1):
        if is_palindrome(n) and is_palindrome(sqrt(n)):
            found += 1
    return found

def parse_input(lines):
    num = int(lines[0])
    cases = lines[1:num + 1]
    return cases

def main():
    import sys
    cases = parse_input(map(lambda a: a.replace("\n", ''), sys.stdin.readlines()))
    for i, case in enumerate(cases, start=1):
        print "Case #%d: %s" % (i, parse_case(case))

if __name__ == '__main__':
    main()




