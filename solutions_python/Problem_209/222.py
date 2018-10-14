from operator import itemgetter
from math import pi

def syrup(ncakes, height):
  cakes = []
  for i in xrange(ncakes):
    cakes.append(map(int, raw_input().strip().split(' ')))
  cakes.sort(key=itemgetter(0,1))
  top_areas = [pi*(cakes[i][0]**2) for i in xrange(ncakes)]
  side_areas = [2*pi*cakes[i][0]*cakes[i][1] for i in xrange(ncakes)]
  scores = {(i,1): side_areas[i] for i in xrange(ncakes)}
  #print scores
  for stackheight in xrange(2, height+1):
    for basecake in xrange(stackheight-1, ncakes):
      #print "calculating %d %d" % (basecake, stackheight)
      basearea = scores[(basecake, 1)]
      maxsubarea = 0
      for topcake in xrange(stackheight-2, basecake):
        #print "finding %d %d" % (topcake, stackheight-1)
        curscore = scores[(topcake, stackheight-1)]
        maxsubarea = max(curscore, maxsubarea)
      scores[(basecake, stackheight)] = basearea + maxsubarea
    #print scores
  maxarea = 0
  for i in xrange(height-1, ncakes):
    curscore = scores[(i, height)] + top_areas[i]
    maxarea = max(curscore, maxarea)
  return maxarea

ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
  ncakes, height = map(int, raw_input().strip().split(' '))
  print "Case #%d: %f" % (i, syrup(ncakes, height))
