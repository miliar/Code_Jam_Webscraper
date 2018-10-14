#!/usr/bin/env python

import re
import sys

def match(words, pattern):
    count = 0
    for word in words:
        if re.match(pattern.replace("(", "[").replace(")", "]"), word):
            count += 1
    return count

def main():
    readline = sys.stdin.readline
    l, d, n = [int(x) for x in readline().split(" ", 2)]
    words = []
    for i in range(d):
        words.append(readline()[:-1])
    for i in range(n):
        pattern = readline()[:-1]
        print "Case #%s: %s" % (i+1, match(words, pattern))

if __name__ == "__main__":
    main()

