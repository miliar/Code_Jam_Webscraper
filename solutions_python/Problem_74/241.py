#!/usr/bin/env python

import sys

def readline():
    return sys.stdin.readline().rstrip("\r\n")

def testcase():
    case_desc = readline().split()
    N = int(case_desc[0])
    pos = {'B': (1,1), 'O': (1,1)}
    other = {'B': 'O', 'O': 'B'}
    seconds = 0
    for i in xrange(N):
        robot = case_desc[2*i+1]
        button = int(case_desc[2*i+2])
        begin, end = pos[robot]
        if button < begin:
            t = begin - button + 1
        elif end < button:
            t = button - end + 1
        else:
            t = 1
        seconds += t
        pos[robot] = (button, button)
        begin, end = pos[other[robot]]
        pos[other[robot]] = begin-t, end+t
    return seconds

def main():
    n_cases = int(readline())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: %d" % (t_case, testcase())

if __name__ == "__main__":
    main()

