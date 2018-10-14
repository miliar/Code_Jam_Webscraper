#!/usr/bin/python
  
def solve():
  N = int(f.pop(0))
  C = [f.pop(0) for i in xrange(N)]
  print C

  # else: return "No"


infile=open("test.in",'r')
f=map(lambda x:x.strip(),infile.readlines())
infile.close()
T=int(f.pop(0))
for t in xrange(T):
  print "Case #" + str(t + 1) + ": " + ("YES" if solve() else "NO")