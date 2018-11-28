#!/usr/bin/env python

import sys

ms = "welcome to code jam"
dict = {}
def gc (need, hay):
    if (hay == ""): return 1;
    if (need == ""): return 0
    if (need,hay) in dict: return dict [need,hay]
    if (need[0] == hay [0]): 
        dict [need,hay] = (gc (need[1:], hay) + gc (need[1:], hay[1:])) % 10000
    else:
        dict [need,hay] =  gc (need[1:], hay) % 10000
        
    return dict[need,hay]

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        print "Case #" + str(i+1) + ": " +  ("%04d" % gc(sys.stdin.readline().strip(), ms))
        dict = {}
main ()
