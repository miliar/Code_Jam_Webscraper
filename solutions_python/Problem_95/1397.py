# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:33:05 2012

@author: mmunnik
"""

f = open("A-small-attempt0.in", 'r')
g = open("A_small_answer.txt", 'w')
N = int(f.readline())

d = {"y": "a", "n": "b", "f": "c", "i": "d", "c": "e", "w": "f", "l": "g", \
    "b": "h", "k": "i", "u": "j", "o": "k", "m": "l", "x": "m", "s": "n", \
    "e": "o", "v": "p", "z": "q", "p": "r", "d": "s", "r": "t", "j": "u", \
    "g": "v", "t": "w", "h": "x", "a": "y", "q": "z", " ": " ", "\n": "\n"}
    
for i,line in enumerate(f):
    g.write("Case #%d: " % (i+1))
    for letter in line:
        g.write(d[letter])

f.close()