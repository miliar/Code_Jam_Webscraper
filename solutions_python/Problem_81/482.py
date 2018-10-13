#!/usr/bin/python
import sys
from decimal import *

getcontext().prec = 12
# Returns gcd of a,b
def gcd(a, b):
  while b != 0:
    t = b
    b = a % b
    a = t
  return a

# Returns (found, index found or to be inserted)
def bs(l, v, s, e):
  if e < s:
    return (False, s - 1)
  m = (s + e) / 2
  if l[m] == v:
    return (True, m)
  elif v < l[m] :
    return bs(l,v,s,m-1)
  else:
    return bs(l,v,m+1,e)

# Sum of permutations
def permute(l, i):
  cl = l[i]
  tsum=0
  for c in cl:
    if i == 0:
      tsum += 1
    else:#conditions here
      tsum +=permute(l,i - 1)
  return tsum



def io(ifp):
  if not ifp:
    ifp = 'input'
  with open(ifp, 'r') as inf:
    with open('output','w') as of:
      lno = 0
      l = inf.readline()[:-1]
      while l:
        lno += 1 
        # Code begins here
        if lno > 1:
          mind = 0
          M = int(l)
          m = []
          while mind < M:
            l = inf.readline()[:-1]
            m.append(l)
            mind += 1
          solve(m)
          ol = "Case #%d:" % (lno - 1)
          of.write(str(ol) + '\n')
          mind = 0
          while mind < M:
            ol = "%0.12f" % rpi[mind]
            of.write(str(ol) + '\n')
            mind += 1
        l = inf.readline()[:-1]

wp = {} # n
owp = {} # n x n 
owwp = {} # n 
oowp = {}# n 
rpi = {}
opc ={}



def solve(m):
  #print m
  global wp, owwp, oowp, rpi
  rpi.clear()
  getwp(m)
  #print wp
  getopc(m)
  #print opc
  getowp(m)
  #print owwp
  getoowp(m)
  #print oowp
  for i in range(len(m)):
    rpi[i] = Decimal('0.25') * wp[i] + Decimal('0.50') * owwp[i] + Decimal('0.25') * oowp[i]

def getopc(m):
  global opc
  opc.clear()
  for i in range(len(m)):
    opc[i] = 0
  for i in range(len(m)):
    for j in range(len(m)):
      if m[i][j] != '.':
        opc[i] += 1



def getowp(m):
  global owp
  global owwp
  owp.clear()
  owwp.clear()
  
  for i in range(len(m)):
    owwp[i] = Decimal('0.0')
    for j in range(len(m)):
      owp[(i,j)] = Decimal('0.0')
  for i in range(len(m)):
    for j in range(len(m)):
      if i != j:
        if m[i][j] == '.':
          continue
        w = 0
        l = 0
        for k in range (len(m)):
          if k != i:
            if m[j][k] == '1':
              w += 1
            if m[j][k] == '0':
              l += 1
        owp[(i,j)] = Decimal(w) / Decimal(w + l)


  for i in range(len(m)):
    for j in range(len(m)):
      owwp[i] += owp[(i,j)]
    owwp[i] /= Decimal(opc[i])



def getoowp(m):
  global oowp, owwp
  oowp.clear()
  for i in range(len(m)):
    oowp[i] = Decimal('0.0')
  for i in range(len(m)):
    for j in range(len(m)):
      if i != j:
        if m[i][j] == '.':
          continue
        oowp[i] += owwp[j]
    oowp[i] /= Decimal(opc[i])


  
def getwp(m):
  global wp
  wp.clear()
  for i in range(len(m)):
    wp[i] = Decimal('0.0');
  for i in range(len(m)):
    w = 0
    l = 0
    for j in range(len(m)):
      if m[i][j] == '1':
        w += 1
      if m[i][j] == '0':
        l += 1
    wp[i] = Decimal(w) / Decimal(w + l)



  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    io(sys.argv[1])
  else:
    io('')



