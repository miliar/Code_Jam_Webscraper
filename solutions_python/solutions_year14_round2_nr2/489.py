#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    fin = open("B-small-0.in", "r")
    fout = open("B-small-0.out", "w")
    T = int(fin.readline())

    for t in xrange(0, T):
        A, B, K = tuple(map(int, fin.readline().strip().split(' ')))
        
        answer = 0
        for i in xrange(0, A):
            for j in xrange(0, B):
                if i & j < K:
                    answer +=1
       
        fout.write("Case #%i: %s\n" % (t+1, answer))
    
    fin.close()
    fout.close()

