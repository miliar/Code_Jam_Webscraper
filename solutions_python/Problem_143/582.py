#!/usr/bin/python

from __future__ import print_function
import re
import fileinput
import sys

def main (): # stdin to stdout; stderr for debugging

    lines = []
    l = 0
    
    for line in fileinput . input ():

        lines . append (line . strip ())
        
    cases = int (lines [l])
    l += 1
    
    for case in range (1, cases + 1):

        numbers = map (int, lines [l] . split (" "))
        l += 1

        A = numbers [0]
        B = numbers [1]
        K = numbers [2]
        
        answer = 0                

        for a in range (0, A):
        
            for b in range (0, B):

                if (a & b) < K:
                
                    answer += 1
            
        reply = "Case #{0}: {1}" . format (case, answer)
        print (reply, file = sys . stderr)
        print (reply)        

if __name__ == "__main__":

    main ()
    exit ()
