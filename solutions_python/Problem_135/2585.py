import sys
rl = lambda: sys.stdin.readline()

def solve(c):
  def getRowAndMap():
    return (int(rl()), [ map(int,rl().strip().split()) for i in range(4)] ) 
      
  r1, i1 = getRowAndMap()
  r2, i2 = getRowAndMap()
  common = set(i1[r1-1]).intersection(set(i2[r2-1]))

  if len(common) == 1:
    print "Case #%d: %d" % (c+1, common.pop())
  elif len(common) > 1:
    print "Case #%d: Bad magician!" % (c+1)
  else:
    print "Case #%d: Volunteer cheated!" % (c+1)

n = int(rl())
for i in range(n):
  solve(i)
