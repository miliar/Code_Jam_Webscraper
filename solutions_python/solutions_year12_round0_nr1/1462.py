#!/usr/bin/env python
import os
import sys

def main():
    filename = sys.argv[1]
    f=open(filename,'r')
    tcCount=int(f.readline(), 10)
    for current_tc in range(tcCount):
        input = f.readline()
        output = ""
        for letter in input:
            if letter ==   'a':
                output += 'y'
            elif letter == 'b':
                output += 'h'
            elif letter == 'c':
                output += 'e'
            elif letter == 'd':
                output += 's'
            elif letter == 'e':
                output += 'o'
            elif letter == 'f':
                output += 'c'
            elif letter == 'g':
                output += 'v'
            elif letter == 'h':
                output += 'x'
            elif letter == 'i':
                output += 'd'
            elif letter == 'j':
                output += 'u'
            elif letter == 'k':
                output += 'i'
            elif letter == 'l':
                output += 'g'
            elif letter == 'm':
                output += 'l'
            elif letter == 'n':
                output += 'b'
            elif letter == 'o':
                output += 'k'
            elif letter == 'p':
                output += 'r'
            elif letter == 'q':
                output += 'z'
            elif letter == 'r':
                output += 't'
            elif letter == 's':
                output += 'n'
            elif letter == 't':
                output += 'w'
            elif letter == 'u':
                output += 'j'
            elif letter == 'v':
                output += 'p'
            elif letter == 'w':
                output += 'f'
            elif letter == 'x':
                output += 'm'
            elif letter == 'y':
                output += 'a'
            elif letter == 'z':
                output += 'q'         
            else:
                output += letter
            
        print "Case #"+str(current_tc+1)+": "+output+"", 
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

