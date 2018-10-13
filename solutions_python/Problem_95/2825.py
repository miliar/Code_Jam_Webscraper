#!/usr/bin/env python
map={' ': ' ',
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

def convert(x):                                    
    str=""
    for i in x:
        str=str+map[i]
    return str

n=input()
num = int(n) 
for i in range(num):
    x=raw_input()
    print "Case #"+ str(i+1) +  ": " + convert(x)
