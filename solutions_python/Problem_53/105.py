#!/usr/bin/env python

import fileinput

def snapper(n, k):
    m = 2**n - 1
    if (k & m) == m:
        return 'ON'
    else:
        return 'OFF'

def main():
    reader = fileinput.input()
    t = int(reader.next())
    for case in range(t):
        n, k = reader.next().strip().split()
        print "Case #%d: %s" % (case + 1, snapper(int(n), int(k)))

main()
