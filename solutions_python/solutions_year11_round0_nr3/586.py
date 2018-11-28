'''
Created on May 7, 2011

@author: ratchet
'''
import itertools
import sys

f = "C-small-attempt0.in"
if len(sys.argv) == 2:
    f = sys.argv[1]
    
file = open(f,"r")

t=int(file.readline())


def rightSide(ls,l):
    rs = list(l)
    for i in ls:
        rs.remove(i)
    return rs
        
def xor(l):
    x = l[0]
    for i in l[1:]:
        x ^= i
    return x        

for ln in range(t):
    N = int(file.readline().strip())
    l = file.readline().strip().split(" ")
    l = [int(i) for i in l]
    ms = -1
    for lsn in range(1,N):
        for ls in itertools.combinations(l,lsn):
            rs = rightSide(ls,l)

            if xor(ls) == xor(rs):
                m = sum(ls)
                m2 = sum(rs)
                if m > ms:
                    ms = m 
                if m2>ms:
                    ms = m2

    if ms == -1:
        ms = "NO"
    print "Case #%d:"%(ln+1),ms
#    break
file.close()