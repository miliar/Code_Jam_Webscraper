#!/usr/bin/env python
from sys import stdin, stdout
from re import compile

if __name__ == '__main__':
    # Read L D N
    L, D, N = map(int, stdin.readline().strip().split())
    
    i = 0
    words = []
    while i < D:
        words.append(stdin.readline().strip())
        i += 1

    i = 0
    while i < N:
        pattern = stdin.readline().strip()
        pattern = pattern.replace("(", "[").replace(")","]")
        cpattern = compile(pattern)
        j = 0
        count = 0
        while j < D:
            if cpattern.search(words[j]):
                count += 1
            j += 1
        stdout.write("Case #%d: %d\n" % (i+1,count))
        i += 1
    
