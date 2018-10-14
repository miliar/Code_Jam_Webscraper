#Kyle Fritz <kyle.p.fritz@gmail.com>
#Code Jam r1b 2010
#problem a
from __future__ import print_function
import sys, csv
    
writeerror=lambda s: sys.stderr.write(s+"\n")

class Leaf:
  def __init__(self):
    self.leaves={}
    
  def getOrMakeLeaf(self,leafname):
    make=leafname not in self.leaves
    if make:
      self.leaves[leafname]=Leaf()
    return (make,self.leaves[leafname])

def addPath(root,path):
  tmade=0
  leaf=root
  for p in path.split('/')[1:]:
    made,leaf=leaf.getOrMakeLeaf(p)
    if made:
      tmade+=1
  return tmade
    
if __name__=="__main__":
  reader = csv.reader(open(sys.argv[1]), delimiter=' ',quoting=csv.QUOTE_NONE)
  getIntList=lambda: list(map(int,reader.next()))
  nCases=getIntList()[0]
  for c in range(nCases):
    N,M=getIntList()
    
    root=Leaf()
    #paths already on fs
    start_dirs=0
    for n in range(N):
      path=reader.next()[0]
      start_dirs+=addPath(root,path)
    writeerror('Case {0}: starting with {1} mkdirs'.format(c+1,start_dirs))
    make_dirs=0
    for m in range(M):
      path=reader.next()[0]
      make_dirs+=addPath(root,path)
    s="Case #{0}: {1}".format(c+1,make_dirs)
    writeerror('\t'+s)
    print(s)

