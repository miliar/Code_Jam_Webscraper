#!/usr/bin/python

def solve():
    pass

def readints(f):
    return map(lambda x: int(x), f.readline().strip().split(' '))

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    [N] = readints(inp)

    for i in range(N):
        [n, k] = readints(inp)
        if (k % pow(2, n)) == (pow(2, n) -1):
            s = 'ON'
        else:
            s = 'OFF'
        print 'Case #%s: %s' % ((i+1), s)
                                
