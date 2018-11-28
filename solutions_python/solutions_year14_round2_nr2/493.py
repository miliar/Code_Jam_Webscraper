import sys
from math import sqrt, floor

T = int(sys.stdin.readline().strip())

def bitand(a,b):
    bina = bin(a)[2:]
    binb = bin(b)[2:]
    al = len(bina)
    bl = len(binb)
    j = min(al,bl)
    r = 0
    for i in range(j):
        if(binb[bl-1-i]=='1') and (bina[al-1-i]=='1'):
            r+=2**(i)
    return r

for trial in range(1, T+1):
  print 'Case #%d:' % trial,

  A,B,K = [int(x) for x in sys.stdin.readline().strip().split()]
  count = 0
  for x in range(A):
    for y in range(B):
        if(bitand(x,y)<K):
            count += 1
  print count