#!/usr/bin/env python

dic = {
'a': 'y', 'b': 'n', 'c': 'f', 'd': 'i', 
'e': 'c', 'f': 'w', 'g': 'l', 'h': 'b', 
'i': 'k', 'j': 'u', 'k': 'o', 'l': 'm', 
'm': 'x', 'n': 's', 'o': 'e', 'p': 'v', 
'q': 'z', 'r': 'p', 's': 'd', 't': 'r', 
'u': 'j', 'v': 'g', 'w': 't', 'x': 'h',
'y': 'a', 'z': 'q',
} 

dic2 = {
'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 
'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 
'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 
'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 
'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 
't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 
'x': 'm', 'z': 'q'
}

import sys

T = int(sys.stdin.readline().strip())
I = 1

while I <= T:
    l = sys.stdin.readline()
    sys.stdout.write('Case #%d: ' % I)
    for i in range(0, len(l)):
        if dic2.has_key(l[i]):
            sys.stdout.write(dic2[l[i]])
        else:
            sys.stdout.write(l[i])

    I += 1
