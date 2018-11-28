from math import *

def solve(prob):
  f=open(prob+'.in','r')
  out=open(prob+'.out','w')
  
  T = int(f.readline())
  for t in range(T):
    (R,k,N)=map(int,f.readline().split())
    g=map(int,f.readline().split())
    ACC=[None]*len(g)  # for each pos: accession no
    POS=[None]*len(g)  # for each acc: pos
    SUM=[None]*len(g)  # for each acc: no sum of income
    acc=0
    pos=0
    sum=0
    res=0
    for i in range(R):
      if ACC[pos] != None:
        acc1=ACC[pos]
        clen=acc-acc1
        csum=sum-SUM[acc1]
        cyc=divmod(R-acc1,clen)
        sum=cyc[0]*csum+SUM[acc1+cyc[1]]
        break
      ACC[pos]=acc
      SUM[acc]=sum
      val=0
      n=0
      while n < N and val+g[pos] <= k:
        val += g[pos]
        pos = (pos+1)%N
        n += 1
      sum += val
      acc += 1
        
    print >>out,'Case #%d: %s'%(t+1,sum)

  f.close()

#  for x in result
  out.close()

#solve(sys.argv[1])
#for i in range(1,11): solve(i)
solve('C-small-attempt0')