# -*- coding: utf-8 -*-

import sys

def solve(s, buf):

    count = 0
    friend = 0
    for i, f in enumerate(buf):
        if i <= count:
            count += f
        elif f != 0:
            friend += i - count
            count += i - count + f

    return friend
    
    
if __name__ == '__main__':
    t = input()

    for i in range(t):
        s, buf = sys.stdin.readline().rstrip().split()

        print 'Case #' + str(i+1) + ':',
        print solve(s, map(int, list(buf)))


