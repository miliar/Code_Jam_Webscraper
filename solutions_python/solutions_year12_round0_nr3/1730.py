#! /usr/bin/python

import string

T = int(raw_input())
t = 1
while t <= T:
    line = raw_input()
    quebra = string.find(line, ' ')
    A = int(line[:quebra])
    B = int(line[quebra+1:])
    m = A
    resp = 0
    while m <= B:
        n = A
        while n < m:
            if string.find(2*str(n), str(m)) != -1:
                resp = resp + 1
            n = n + 1
        m = m + 1
    print 'Case #' + str(t) + ':', resp
    t = t + 1



