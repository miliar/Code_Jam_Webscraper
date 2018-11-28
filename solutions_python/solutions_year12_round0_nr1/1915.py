#!/usr/bin/env python

ttab = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def inp(fin):
    return [eval(x) for x in fin.readline().strip().split()]

def transline(line):
    newl = [ttab[c] for c in list(line)]
    return "".join(newl)

def solveCase(fin):
    line = fin.readline().strip()
    newline = transline(line)
    return newline

def solve(fin):
    [ncase] = inp(fin)
    for i in xrange(ncase):
        print "Case #%d: %s" % (i+1, solveCase(fin))

def main():
    import sys
    solve(sys.stdin)

if __name__ == "__main__":
    main()

