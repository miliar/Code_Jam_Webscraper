#!/usr/bin/env python

import sys

qmult = {
  '1': {'1': '1', '-1': '-1', 'i': 'i', '-i': '-i', 'j': 'j', '-j': '-j', 'k': 'k', '-k': '-k'},
  '-1': {'1': '-1', '-1': '1', 'i': '-i', '-i': 'i', 'j': '-j', '-j': 'j', 'k': '-k', '-k': 'k'},
  'i': {'1': 'i', '-1': '-i', 'i': '-1', '-i': '1', 'j': 'k', '-j': '-k', 'k': '-j', '-k': 'j'},
  '-i': {'1': '-i', '-1': 'i', 'i': '1', '-i': '-1', 'j': '-k', '-j': 'k', 'k': 'j', '-k': '-j'},
  'j': {'1': 'j', '-1': '-j', 'i': '-k', '-i': 'k', 'j': '-1', '-j': '1', 'k': 'i', '-k': '-i'},
  '-j': {'1': '-j', '-1': 'j', 'i': 'k', '-i': '-k', 'j': '1', '-j': '-1', 'k': '-i', '-k': 'i'},
  'k': {'1': 'k', '-1': '-k', 'i': 'j', '-i': '-j', 'j': '-i', '-j': 'i', 'k': '-1', '-k': '1'},
  '-k': {'1': '-k', '-1': 'k', 'i': '-j', '-i': 'j', 'j': 'i', '-j': '-i', 'k': '1', '-k': '-1'}}

def ijk(string):
    seg1 = '1'
    seg2 = '1'
    seg3 = '1'
    seg4 = '1'
    k = 0
    while seg1 != 'i':
        if k >= len(string):
            return "NO"
        seg1 = qmult[seg1][string[k]]
        k += 1
    while seg2 != 'j':
        if k >= len(string):
            return "NO"
        seg2 = qmult[seg2][string[k]]
        k += 1
    while seg3 != 'k':
        if k >= len(string):
            return "NO"
        seg3 = qmult[seg3][string[k]]
        k += 1
    while k < len(string):
        seg4 = qmult[seg4][string[k]]
        k += 1
    if seg4 == '1':
        return "YES"
    return "NO"

t = int(sys.stdin.readline())
for i in range(0,t):
    (ls, xs) = sys.stdin.readline().split(' ')
    string = sys.stdin.readline()[:-1] * int(xs)
    print "Case #" + str(i+1) + ": " + ijk(string)
