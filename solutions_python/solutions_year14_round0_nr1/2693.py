#!/usr/bin/python

import sys

def read_obj(cls):
    return cls(sys.stdin.readline().strip())

def read_obj_list(cls):
    return map(cls, sys.stdin.readline().strip().split())

def read_nth_row(n):
    for i in xrange(4):
        tmp = read_obj_list(int)
        if i == n - 1:
            res = tmp
    return set(res)

def solve():
    t = read_obj(int)
    for i in xrange(1, t + 1):
        ans1 = read_obj(int)
        row1 = read_nth_row(ans1)
        ans2 = read_obj(int)
        row2 = read_nth_row(ans2)
        res = row1 & row2
        print "Case #%d:" % i,
        if len(res) == 1:
            print res.pop()
        elif len(res) == 0:
            print "Volunteer cheated!"
        else:
            print "Bad magician!"

if __name__ == "__main__":
    solve()
