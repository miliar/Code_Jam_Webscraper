#!/usr/bin/python

import sys

inputFile = 'B-large.in'
f = open(inputFile, 'r')

def main(argv):
    T = int(f.readline())
    for i in range(1, T+1):
        N = f.readline()[:-1]
        print("Case #%r: %s" % (i, getMaxTidy(N)))

def getMaxTidy(N):
    l = [int(i) for i in N]
    i = 1
    while i < len(l) and l[i] >= l[i-1]:
        i += 1
    if i==len(l):
        return N
    j = i-1
    while j > 0 and l[j] == l[j-1]:
        j -= 1
    l[j] -= 1

    for k in range(j+1, len(l)):
        l[k] = 9

    return str(int(''.join(str(i) for i in l)))

if __name__ == '__main__':
    main(sys.argv[1:])

