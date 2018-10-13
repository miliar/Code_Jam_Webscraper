#!/usr/bin/env python

import sys

def groupsToGo(queue, k):
    result = 0
    s = 0
    i = 0
    for i in range(len(queue)):
        if s + queue[i] <= k:
            s += queue[i]
        else:
            return i
    return len(queue)
    

def solve(r, k, queue):
    result = 0
    for i in range(r):
        x = groupsToGo(queue, k)
        result += sum(queue[:x])
        queue = queue[x:] + queue[:x]
    return result
        

def main():
    t = int(sys.stdin.readline())
    for i in range(0, t):
        r, k, n = map(int, sys.stdin.readline().split())
        gs = map(int, sys.stdin.readline().split())
        print 'Case #%d: %s' % (i + 1, solve(r, k, gs))


if __name__ == '__main__':
    sys.exit(main())
