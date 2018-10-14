#! /usr/bin/env python

import sys

# this program works with python version 2.3.4

if ( len(sys.argv) > 1 ) : file = open(sys.argv[1], "r")
else : file = sys.stdin

def readline() : return file.readline().rstrip()

def getint() : return int(readline())

def getarray() : return [int(i) for i in readline().split()]

def result(n) : return 'Case #' + str(n) + ':'


sd = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def ssd(n, b) :
    if n < b : return sd[n]
    return sd[n % b] + ssd(n / b, b)


def happy(n, b) :
    v = {}
    while (1) :
        s = ssd(n, b)
        if s == 1  : return 1
        if s in v : return 0
        v[s] = ''
        n = s

def happybase(bases) :
    n = 2
    while ( 1 ) :
        for i in range(len(bases)) :
            if not happy(n, bases[i]) : break
        else :
            return n
        n += 1

T = getint()
for i in range(1, T +1) :
    print result(i), happybase(getarray())

