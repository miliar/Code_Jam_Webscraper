import sys,collections
import os

#NAME = 'A-example'
#NAME = 'A-small-attempt0'
NAME = 'A-large'

BASEDIR = os.path.expanduser('~/Projects/Challenge/Google CodeJam/GCJ 2010 Round 1B/%s')
inname  = BASEDIR % (NAME + '.in')
outname = BASEDIR % (NAME + '.out')

with open(inname) as fin:
    with open(outname,'w') as fout:
        num_cases = int(fin.readline())
        for case_idx in range(1,1+num_cases):
            N,M = map(int,fin.readline().split())
            A = set( tuple(fin.readline()[:-1].split('/')) for n in range(N) )
            B = [tuple(fin.readline()[:-1].split('/')) for m in range(M)]

            answer = 0
            for b in B:
                for i in range(1,len(b)):
                    if b[:i+1] not in A:
                        A.add(b[:i+1])
                        answer += 1
                        #print "added", b[:i+1]

            #print answer               
            print >> fout, "Case #%d: %d" % (case_idx, answer)
