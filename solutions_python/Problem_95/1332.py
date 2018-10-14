#!/usr/bin/env python

import sys

mapping = dict({
    'a':'y',
    'b':'h',
    'c':'e',
    'd':'s',
    'e':'o',
    'f':'c',
    'g':'v',
    'h':'x',
    'i':'d',
    'j':'u',
    'k':'i',
    'l':'g',
    'm':'l',
    'n':'b',
    'o':'k',
    'p':'r',
    'q':'z',
    'r':'t',
    's':'n',
    't':'w',
    'u':'j',
    'v':'p',
    'w':'f',
    'x':'m',
    'y':'a',
    'z':'q'
})

def main():
    n = int(sys.stdin.readline())
    for i in range(1, n+1):
        line = sys.stdin.readline()[:-1]

        print 'Case #{0}: {1}'.format(i, speaking_with_tongues(line))

def speaking_with_tongues(s):
    ret = ''
    for i, c in enumerate(s):
        if c in mapping:
            ret += mapping[c]
        else:
            ret += c
    return ret

if __name__ == '__main__':
	main()
