#!/usr/bin/env python2
import sys

def main():
    infile = sys.stdin
    T = infile.readline()
    case = 1
    for line in infile.readlines():
        Smax = int(line.split()[0])
        S = [int(i) for i in line.split()[1]]
        nFriend = 0
        standing = 0
        for shyness, s in enumerate(S):
            if s and standing <  shyness:
                nFriend += shyness - standing
                standing += nFriend + s
            else:
                standing += s
            
        print "Case #%d: %d" %(case, nFriend)
        case += 1

if __name__ == '__main__':
    main()

