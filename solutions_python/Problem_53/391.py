#! /usr/bin/env python

import sys

# this program works with python version 2.3.4

if ( len(sys.argv) > 1 ) : file = open(sys.argv[1], "r")
else : file = sys.stdin

def getstr() : return file.readline().rstrip()

def getint() : return int(getstr())

def getfp() : return float(getstr())

def getarray() : return getstr().split()

def getintarray() : return [int(i) for i in getarray()]

def getfparray() : return [float(i) for i in getarray()]

def result(n,a) : return 'Case #' + str(n) + ': ' + a

T = getint()

for i in range(1, T + 1) :
    N, K = getintarray()
    K += 1
    while N :
        if K & 1 :
            K = 0
            break
        N -= 1
        K >>= 1
    if K == 0 :
        print result(i, 'OFF')
    else :
        print result(i, 'ON')

