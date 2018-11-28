#!/usr/bin/python
import sys


def getstate(n, k):
    """
    returns boolean for the current state
    True: ON
    False: OFF
    """
    return ( k % (2**n) == 2**n - 1)


def main():
    data = sys.stdin.readlines()
    assert(len(data[1:]) == int(data[0]))
    
    for i, line in enumerate(data[1:]):
        n, k = map(int, line.split(' '))
        state = getstate(n, k)
        if state == True:
            print "Case #"+str(i+1)+": ON"
        else:
            print "Case #"+str(i+1)+": OFF"
             

if __name__ == '__main__':
    main()
