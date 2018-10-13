#!/usr/bin/env python
# encoding: utf-8

import sys
import os

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n, k = map(int, sys.stdin.readline().split())
        print "Case #%d: %s" % (i + 1, "ON" if k % 2 ** n == 2 ** n - 1 else "OFF")

if __name__ == '__main__':
	main()

