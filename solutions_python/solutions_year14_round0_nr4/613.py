#!/usr/bin/python
  
def solve():
  NUM = int(f.pop(0))
  N = sorted(map(float,f.pop(0).split()),reverse=True)
  K = sorted(map(float,f.pop(0).split()),reverse=True)
  return str(deceitful(N,K))+' '+str(war(N,K))
  
def war(a,b):
  N,K=[],[]
  N.extend(a)
  K.extend(b)
  p = 0
  while len(N) or len(K):
    if K[0]<N[0]:
      K.pop() 
      N.pop(0)
      p+=1
    else:
      K.pop(0) 
      N.pop(0)
  return p  
    
def deceitful(a,b):
  N,K=[],[]
  N.extend(a)
  K.extend(b)
  p = 0
  all = sorted(N+K,reverse=True)
  r = [1 if i in N else 0 for i in all]
  while len(r)>0:
    idx = pair(r)
    if idx>=0:
      p+=1
      r.pop(idx+1)
      r.pop(idx)
    else:
      break
  return p

def pair(x): #1,0
  for i in xrange(0,len(x)-1):
    if x[i]==1 and x[i+1]==0:
      return i
  else: return -1
  
infile=open("D-large.in",'r')
f=map(lambda x:x.strip(),infile.readlines())
infile.close()
T=int(f.pop(0))
for t in xrange(T):
  print "Case #" + str(t + 1) + ": " + str(solve())