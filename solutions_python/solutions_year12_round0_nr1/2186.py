#!/usr/bin/env python
# manuel zubieta
# april 14th, 2012
# google codejam qualification round problem 1

code = {
    'a' : 'y', 'b' : 'h', 'c' : 'e',
    'd' : 's', 'e' : 'o', 'f' : 'c',
    'g' : 'v', 'h' : 'x', 'i' : 'd',
    'j' : 'u', 'k' : 'i', 'l' : 'g',
    'm' : 'l', 'n' : 'b', 'o' : 'k',
    'p' : 'r', 'q' : 'z', 'r' : 't',
    's' : 'n', 't' : 'w', 'u' : 'j',
    'v' : 'p', 'w' : 'f', 'x' : 'm',
    'y' : 'a', 'z' : 'q', ' ' : ' '
}

def solve ( n ):
    print 'Case #%s: ' % n,
    rawline = raw_input()
    text = ""
    for c in rawline:
        text += code[c]

    print text

if __name__ == "__main__":
    n = input()
    for i in xrange(1, n+1):
        solve(i)
