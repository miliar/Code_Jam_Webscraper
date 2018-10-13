#!/usr/bin/env python

import re

def main():
    L, D, N = map(int, raw_input().split())

    dic = [raw_input() for _ in range(D)]

    for i in range(N):
        pattern = raw_input().replace('(', '[').replace(')', ']')
        regexp = re.compile(pattern)
        print "Case #%d:" % (i+1), sum(1 for key in dic if regexp.match(key))

    
if __name__ == "__main__":
    main()
