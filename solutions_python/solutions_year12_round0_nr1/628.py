#!/usr/bin/python
#A.py
#Author: James Damore
#Created on: April 14, 2012
#Time-stamp: <2012-04-14 13:32:18>
#cat Downloads/-small-attempt0.in | ~/python/codeJam/A.py > output.txt

import math, sys
import codejam as cj

def dbgln(a): sys.stderr.write(str(a) + "\n")
def read_ints(lines = None):
    if lines is None: return map(int, raw_input().split())
    return [map(int, raw_input().split()) for _ in range(lines)]


d = {' ': ' ',
     'a': 'y',
     'b': 'h',
     'c': 'e',
     'd': 's',
     'e': 'o',
     'f': 'c',
     'g': 'v',
     'h': 'x',
     'i': 'd',
     'j': 'u',
     'k': 'i',
     'l': 'g',
     'm': 'l',
     'n': 'b',
     'o': 'k',
     'p': 'r',
     'q': 'z',
     'r': 't',
     's': 'n',
     't': 'w',
     'u': 'j',
     'v': 'p',
     'w': 'f',
     'x': 'm',
     'y': 'a',
     'z': 'q'}


def read_input():
    s = raw_input()
    return ''.join([d[S] for S in s])

    #return output


numCases=input()
for i in range(1, numCases+1):
    #read_input()
    #dbgln(i)
    output = read_input()
    print "Case #%d:" % i, output
