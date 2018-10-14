#! /usr/bin/python 2.7

import time
import sys

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines[0])
    for case in range(T):
        givencase = case + 1
        line = lines[givencase].split()
        cookies(givencase,int(line[0]),int(line[1]),int(line[2]))
    f.close()

def cookies(case,A,B,K):
    counter = 0
    if (A < B):
        shorter = A
        longer = B
    else:
        shorter = B
        longer = A

    for i in range(shorter):
        for j in range(longer):
            result = i & j
            if result < K:
                counter += 1

    print "Case #"+str(case)+":",counter
    sys.stdout.flush()

if __name__ == '__main__':
    main()
