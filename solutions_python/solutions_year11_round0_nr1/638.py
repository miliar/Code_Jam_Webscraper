#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

def solve():
    values = read_line().split(' ')
    N = int(values[0])
    buttons = []
    for i in range(1, len(values)):
        if i % 2 == 1:
            buttons.append(0 if values[i] == 'O' else 1)
        else:
            buttons.append(int(values[i]))

    robots = [1, 1]
    sec = 0
    for i in range(0, len(buttons), 2):
        r1 = buttons[i]
        r2 = (r1 + 1) % 2
        t = abs(robots[r1] - buttons[i + 1]) + 1
        sec += t
        robots[r1] = buttons[i + 1]
        for j in range(i+2, len(buttons), 2):
            if buttons[j] == r2:
                m = min(t, abs(robots[r2] - buttons[j+1]))
                if buttons[j+1] > robots[r2]:
                    robots[r2] += m
                else:
                    robots[r2] -= m
                break
    print sec
        

def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
