#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 13 Apr 2013

@author: Artem
'''
from __future__ import division
import os
import sys
import time


def write_case(f_out, out, k):
    out = "Case #%d: %s\n" % (k, out)
    f_out.write(out)
    #print out

def solve(f_in, f_out):
    T = f_in.readline()
    if not T:
        print 'The input file is empty!'
        sys.exit()
    T = int(T)
    
    for k in xrange(1, T+1):
        N, M = f_in.readline().split()
        N = int(N)
        M = int(M)
        
        pos = True
        
        lawn = []
        for _ in xrange(N):
            s = f_in.readline().split()
            s = ''.join(s)
            lawn.append(s)
        
        if N >= 1 and M >= 1:         
            for i in xrange(0, N):
                for j in xrange(0, M):
                    ed1 = True
                    ed2 = True
                    #edg1 = [int(lawn[0][j]), int(lawn[N-1][j])]
                    #edg2 = [int(lawn[i][0]), int(lawn[i][M-1])]
                    edg1 = [int(x) for x in lawn[i]]
                    edg2 = []
                    for x in xrange(N):
                        s = lawn[x][j]
                        edg2.append(int(s))
                    
                    edg1 = list(set(edg1))
                    edg2 = list(set(edg2))
                    
                    gr = int(lawn[i][j])
                    """
                    if edg1[0] > gr or edg1[1] > gr:
                        ed1 = False
                    if edg2[0] > gr or edg2[1] > gr:
                        ed2 = False
                    """
                    for x in edg1:
                        if x > gr:
                            ed1 = False
                            break
                        
                    for x in edg2:
                        if x > gr:
                            ed2 = False
                            break
                    
                    if not ed1 and not ed2:
                        pos = False
                        break
        
        
        if pos:
            out = 'YES'
        else:
            out = 'NO'
        write_case(f_out, out, k)

def main():
    START = time.time()
    my_dir = os.getcwd()
    name = os.path.basename(__file__)[:-3:]
    
    file_in = "%s\\input\\%s.in" % (my_dir, name)
    file_out = "%s\\output\\%s.out" % (my_dir, name)
    with open(file_in, 'a+') as f_in:
        with open(file_out, 'w') as f_out:
            solve(f_in, f_out)
    
    print 'All done in %f s' % (time.time()-START)
    
if __name__ == '__main__':
    main()