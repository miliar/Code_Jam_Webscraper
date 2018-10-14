import sys, re

class fol(object):
  name = ""
  ch = None
  def __init__(self,name):
    self.name = name
    self.ch=[]

  def add(self, path):
    if len(path)==0: return 0
    cur = path[0]
    path = path[1:len(path)]
    found = 0
    res = 0
    for c in self.ch:
      if c.name==cur:
        res += c.add(path)
        found = 1
        break
    if not found:
      chil = fol(cur)
      self.ch.append(chil)
      res+=1
      res+=chil.add(path)
    return res

cases = sys.stdin.readline()

for ii in range(0,int(cases)):
  N,M = [int(x) for x in sys.stdin.readline().split()]

  root = fol("")
  for i in range(0,N):
    str = sys.stdin.readline()
    path = str[1:len(str)-1].split("/")
    root.add(path)
  res = 0
  for i in range(0,M):
    str = sys.stdin.readline()
    path = str[1:len(str)-1].split("/")
    res += root.add(path)
  print "Case #%d: %d" % (ii+1,res)

