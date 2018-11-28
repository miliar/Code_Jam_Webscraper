#!/usr/bin/python

ifn = 'sample.in'
ofn = 'sample_ans.txt'

ifn = 'D-small-attempt2.in'
ofn = 'D-small-ans.txt'

ifn = 'D-large.in'
ofn = 'D-large-ans.txt'

ofp = open(ofn, 'w')

def war(blk, N):
        s, wcnt = 0, N
        for i in range(N):
                for j in range(s,N):
                        if(blk[1][j] > blk[0][i]):
                                wcnt = wcnt - 1
                                break
                s = j + 1
                if s == N:
                        break
        return wcnt

def dwar(blk, N):
        s = 0
        for i in range(N):
                if blk[0][i] > blk[1][s]:
                        s = s + 1
        return s

with open(ifn, 'r') as ifp:
        T = (int)(ifp.readline())
        for i in range(T):
                N = (int)(ifp.readline())
                blk = []
                for j in range(2):
                        line = ifp.readline()
                        blk.append([float(p) for p in line.split(' ')])
                        blk[j].sort()
                                        
                ofp.write("Case #%d: %d %d\n" % (i+1, dwar(blk, N), war(blk,N)))
ifp.close()
ofp.close()
