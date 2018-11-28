#!/usr/bin/env python
import os
import sys

def main():
    filename = sys.argv[1]
    f=open(filename,'r')
    tcCount=int(f.readline(), 10)
    for current_tc in range(tcCount):
        line = f.readline().split(' ')
        start = int(line[0], 10)
        end = int(line[1], 10)
        count = 0
        
        current = start
        while current < end:
            curstr = str(current)
            seclist = []
            for flipc in range(1, len(curstr)):
                newstr = curstr[flipc:]+curstr[0:flipc]
                if newstr[0] != '0':
                    new = int(newstr, 10)                   
                    if new > current and new <= end and new not in seclist:
                        count += 1 
                        seclist.append(new)
            
            current += 1
        
        print "Case #"+ str(current_tc+1) + ": " + str(count) 
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

