#!/usr/bin/python

from sys import stdin

code = {' ': ' ',
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

def translate(a):
    at = ""
    for i in range(len(a)):
        at += code[a[i]]
    return at

ncases = int(stdin.readline().strip())

for i, line in enumerate(stdin.xreadlines()):
    line = line.strip()
    print("Case #%i: %s" % (i+1, translate(line)))
