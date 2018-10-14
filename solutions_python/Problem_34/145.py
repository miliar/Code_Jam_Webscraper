# -*- coding: utf-8 -*-
from sys import stdin

def pat(s):
    i = 0
    x = []
    while i < len(s):
        if s[i] == '(':
            j = s.find(')', i)
            x.append(set(s[i+1:j]))
        else:
            x.append(set(s[i],))
            j = i
        i = j+1
    return x

l, d, n = map(int, stdin.readline().split())
words = [stdin.readline().strip() for _ in xrange(d)]

def main():
    pattern = pat(stdin.readline().strip())
    return str(len(filter(lambda w:all(map(lambda x:x[0] in x[1], zip(w, pattern))), words)))

for i in xrange(0, n):
    print "Case #%d: %s"%(i+1, main())
