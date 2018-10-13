import sys
import itertools
import numpy as np
import math
from copy import copy
f=open(sys.argv[1],'r')
ncases=int(f.readline().strip('\n'))
def isFAS(x):
  xs=repr(x)
  if int(x)!=x or xs!=xs[::-1]:
    return False
  sr=sqrt(x)
  ssr=repr(int(sr))
  if int(sr)!=sr or ssr!=ssr[::-1]:
    return False
  return True

def sqisFAS(x):
  xs=repr(x)
  if int(x)!=x or xs!=xs[::-1]:
    return 0
  sq=x*x
  ssq=repr(int(sq))
  if int(sq)!=sq or ssq!=ssq[::-1]:
    return 0
  return 1

def get_len_p1(ls):
  """
  Must start from even number.
  """
  l=len(str(ls[0]))
  out=[]
  sp=l/2
  for c in ls:
    for i in xrange(3):
      sc=str(int(c))[:sp]
      x=int(sc+str(i)+sc[::-1])
      xx=x**2
      sxx=repr(xx).strip('L')
      if str(xx)==sxx[::-1]:
        out.append(x)
  return out
        
def get_len_p2(ls):
  """
  Must start from even number.
  """
  l=len(str(ls[0]))
  out=[]
  sp=l/2
  for c in ls:
    for i in xrange(3):
      sc=str(int(c))[:sp]
      x=int(sc+str(i)*2+sc[::-1])
      xx=x**2
      sxx=repr(xx).strip('L')
      if str(xx)==sxx[::-1]:
        out.append(x)
  return out

def get_len(l):
  fas=[]
  ll=(int(l)/2+(int(l)%2))-1
  ctr=0
  if l%2==0:
    for x in xrange(10**ll,10**(ll+1)):
      xx=int(str(x)+str(x)[::-1])**2
      sxx=repr(xx).strip("L")
      if sxx==sxx[::-1]:
        fas.append(np.sqrt(xx))
      ctr=ctr+(sxx==sxx[::-1])
  else:
    for x in xrange(10**ll,10**(ll+1)):
      xx=int(str(x)[:-1]+str(x)[::-1])**2
      sxx=repr(xx).strip("L")
      if sxx==sxx[::-1]:
        fas.append(np.sqrt(xx))
      ctr=ctr+(sxx==sxx[::-1])
  return fas  
    
def get_fas(B):
  #Want all fas from length 1 to lB 
  lB=len(str(B))
  #Start with the manual buggers
  nos=[]
  if lB>1:
    nos.extend([1,2,3])
  if lB>2:
    nos.extend([11,22])
  curr=2
  seed=[11,22]
  while True:
    if curr+1<=lB:
      nos.extend(get_len_p1(seed))
      curr=curr+1
    if curr+1<=lB:
      seed=get_len_p2(seed)
      nos.extend(seed)
      curr=curr+1
    else:
      break
  return nos

badboys=[x**2 for x in get_fas(10**50)]
vbadboys=[]
for i in xrange(1,11):
  vbadboys.extend([int(x)**2 for x in get_len(i)])
    
for icase in xrange(ncases):
  A,B=[int(x) for x in f.readline().strip().split()]
  #Only need to look at integers from floor(sqrt(A))-floor(sqrt(B))
  #gctr=0
  #for i in xrange(int(np.ceil(np.sqrt(A))),int(np.floor(np.sqrt(B))+1)):
  #  t=sqisFAS(i)
  #  gctr=gctr+t
  ctr=0
  for i in xrange(len(badboys)):
    ctr=ctr+(badboys[i]>=A and badboys[i]<=B)
    #t=sqisFAS(i)
    #if t==1:
    #  print "Winner %d %d"%(i,i*i)
    #ctr=ctr+sqisFAS(i)
  #if ctr!=gctr:
  #  print "DANGER WILL ROBINSON!"
  #  break
  print "Case #%d: %d"%(icase+1,ctr)
