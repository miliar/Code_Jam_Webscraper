#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def isTidy(s):
    previous = int(s[0])
    for c in s[1:]:
        current = int(c)
        if previous > current:
            return False
        previous = current
    return True

def list_minus_1(l):
    if l[-1] == '0':
        l[-1] = '9'
        return list_minus_1(l)
    l[-1] = str(int(l[-1]) - 1)
    return l

def getLastTidyNum(s):
    if isTidy(s):
        return s
    list_c = list(s)
    i = len(list_c) - 1
    while i > 0:
        if isTidy(list_c[:i+1]):
            i = i - 1
            continue
        list_c[i] = '9'
        minus_idx = i - 1
        while minus_idx >= 0 and list_c[minus_idx] == '0':
            list_c[minus_idx] = '9'
            minus_idx = minus_idx - 1
        i = minus_idx + 1
        list_c[minus_idx] = str(int(list_c[minus_idx]) - 1)
        i = i -1

    return ''.join(list_c).lstrip('0')

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input()
    print "Case #{}: {}".format(i, getLastTidyNum(s))
