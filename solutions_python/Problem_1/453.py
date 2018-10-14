#!/usr/bin/python
calculated={}
def compute(s_engines,queries,maxv):
   if len(queries)==0:
      return 0
   if calculated.has_key(tuple(queries)):
      return calculated[tuple(queries)]
   val=maxv
   for se in s_engines:
      i=0
      while i<len(queries):
         if queries[i] == se:
            break;
         i+=1
      if i>0:   
         q2=queries[i:]
         c=compute(s_engines,q2,maxv)
         if c<maxv:
            maxv=c
   calculated[tuple(queries)]=maxv+1
   return maxv+1
   
if __name__ == "__main__":
   import sys
   sys.setrecursionlimit(1000000)
   N = int(sys.stdin.readline())   
   for i in xrange(N):
      S = int(sys.stdin.readline())
      s_engines=[]
      for j in xrange(S):
         s_engines.append(sys.stdin.readline().strip())
      Q = int(sys.stdin.readline())
      queries=[]
      for j in xrange(Q):
         queries.append(sys.stdin.readline().strip())
      print "Case #%d: %d" %(i+1,max(compute(s_engines,queries,len(queries))-1,0))

