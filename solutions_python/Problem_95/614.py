#!/usr/env/python

d = {
    'a': 'y',#    
    'b': 'h',#
    'c': 'e',#
    'd': 's',#
    'e': 'o',#
    'f': 'c',#
    'g': 'v',#
    'h': 'x',#
    'i': 'd',#
    'j': 'u',#
    'k': 'i',#
    'l': 'g',#
    'm': 'l',#
    'n': 'b',#
    'o': 'k',#
    'p': 'r',#
    'q': 'z',#
    'r': 't',#
    's': 'n',#
    't': 'w',#
    'u': 'j',#
    'v': 'p',#
    'w': 'f',#
    'x': 'm',#
    'y': 'a',#
    'z': 'q'#
}

n = int(raw_input())

for i in range(n):
        line = raw_input()
        res = ""
        for c in line:
            if c in d:
                res += d[c]
            else:
                res += c
        print "Case #" + str(i+1) + ": " + res
                
