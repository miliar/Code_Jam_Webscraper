#!/usr/bin/python
def perm(a,s):
   ps=""
   for i in xrange(len(s)/len(a)):
      for j in xrange(len(a)):
         ps+=s[a[j]+len(a)*i]
   return ps
   
def csize(s):
   c=1
   p=s[0]
   for i in xrange(1,len(s)):
      if s[i]!=p:
         c+=1
         p=s[i]
   return c    

def all_perms(a):
    if len(a) <=1:
        yield a
    else:
        for perm in all_perms(a[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + a[0:1] + perm[i:]

def solve(s,K):
   minc=len(s)
   for p in all_perms(range(K)):
      c=csize(perm(p,s))
      if c<minc:
         minc=c
   return minc
   
if __name__ == "__main__":
   import sys
   sys.setrecursionlimit(1000000)
   N = int(sys.stdin.readline())   
   for i in xrange(N):
      K = int(sys.stdin.readline())   
      s = sys.stdin.readline()
      print "Case #%d: %d" %(i+1,solve(s,K))
