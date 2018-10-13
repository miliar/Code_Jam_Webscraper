import math

def solve(n, cells):
  data = set()
  for cell in cells:
    for x in xrange(cell[0], cell[2] + 1):
      for y in xrange(cell[1], cell[3] + 1):
        data.add((x,y))
  
  #for d in data: print d,
  #print

  count = 0
  while len(data) > 0:
    count += 1
    ndata = {}
    for d in data:
      ndata[(d[0],d[1])] = ndata.get((d[0],d[1]),0) + 1
      ndata[(d[0],d[1]+1)] = ndata.get((d[0],d[1]+1),0) + 1
      ndata[(d[0]+1,d[1])] = ndata.get((d[0]+1,d[1]), 0) + 1
    data = set()
    for d,c in ndata.iteritems():
      if c > 1: 
        data.add(d)
        #print d,
    #print


  return count


lines = open("input.txt").readlines()
cases = int(lines[0])
line = 1

for case in xrange(1, cases + 1):
    n = int(lines[line])
    line += 1
    cells = []
    for i in xrange(n):
       cells.append([int(x) for x in lines[line+i].strip("\n").split()])
    line += n
    print "Case #%d: %d" % (case, solve(n,cells))
    
