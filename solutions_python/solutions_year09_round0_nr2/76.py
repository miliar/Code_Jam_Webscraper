import psyco
#psyco.full()

import sys
import re
import os
from pprint import pprint

class DSU(object):
    def __init__(self):
        self.parent = self
        self.rank = 0
    def representative(self):
        if self.parent is self:
            return self
        self.parent = self.parent.representative()
        return self.parent
    def union(self,other):
        self = self.representative()
        other = other.representative()
        if self is other:
            return
        if self.rank < other.rank:
            self.parent = other
        elif self.rank > other.rank:
            other.parent = self
        else:
            other.parent = self
            self.rank += 1

if len(sys.argv) != 2:
    print 'specify input file'
    exit()
    
with open(sys.argv[1]) as fin:
    lines = fin.readlines()

cases = []
    
T = int(lines[0])
k = 1
for i in range(T):
    H,W = map(int,lines[k].split())
    cases.append([map(int,s.split()) for s in lines[k+1:k+1+H]])
    k += H+1

#pprint(cases)    

fout = open(os.path.splitext(sys.argv[1])[0]+'.out','wt')
    
for caseNo,case in enumerate(cases):
    print '\b'*10,100*caseNo/len(cases),'%',
    H = len(case)
    W = len(case[0])
    inf = 100000
    case = [[inf]*W]+case+[[inf]*W]
    case = [[inf]+s+[inf] for s in case]
    
    basins = [[DSU() for k in range(W)] for j in range(H)]
    for j in range(H):
        for k in range(W):
            deltas = (0,0),(-1,0),(0,-1),(0,1),(1,0)
            q = [case[j+dj+1][k+dk+1] for dj,dk in deltas]
            mq = min(q)
            d = q.index(mq)
            dj,dk = deltas[d]
            basins[j][k].union(basins[j+dj][k+dk])
            
    labels = {}
    letter = 'a'
    result = []
    for j in range(H):
        result.append([])
        for k in range(W):
            b = basins[j][k].representative()
            if b not in labels:
                labels[b] = letter
                letter = chr(ord(letter)+1)
            result[-1].append(labels[b])
    
    print>>fout, 'Case #%s:'%(caseNo+1)
    for j in range(H):
        print>>fout, ' '.join(result[j])
            
fout.close()    
print

