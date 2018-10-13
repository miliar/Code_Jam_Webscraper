#!/usr/bin/env python

import sys

class Key:
    def __init__(self):
        self.letters = []
    
    def __repr__(self):
        return str(self.letters)

def main():
    if len(sys.argv) == 1:
        f = open('test.in')
    else:
        f = open(sys.argv[1])

    count = int(f.readline())
    for i in xrange(1, count + 1):

        dt1 = f.readline().strip().split()
        P = int(dt1[0])
        K = int(dt1[1])
        L = int(dt1[2])
        
        dt2 = f.readline().strip().split()
        
        freq = []
        for it in dt2:
            freq.append(int(it))
        
        freq.sort(reverse=True)
        
        keys = []
        for k in xrange(K):
            keys.append(Key())
        
        for fr in freq:
            min_l = P
            min_key = None
            for key in keys:
                l = len(key.letters)
                if l < min_l:
                    min_l = l
                    min_key = key
                    if min_l == 0:
                        break
            min_key.letters.append(fr)

        result = 0

        for key in keys:
            l = len(key.letters)
            for k in xrange(l):
                result += key.letters[k] * (k + 1)
        
        print 'Case #%d: %d' % (i, result)

if __name__ == '__main__':
    main()
