import os, sys

ncases = int( raw_input() )

for n in xrange(ncases):
  #read input
  first = int (raw_input() )
  fdeck = []
  for i in xrange(4):
    row = []
    for j in raw_input().strip().split(" "):
      #import pdb; pdb.set_trace()
      row.append( int(j) )
    fdeck.append(row)
  second = int (raw_input() )
  sdeck = []
  for i in xrange(4):
    row = []
    for j in raw_input().strip().split(" "):
      row.append( int(j) )
    sdeck.append(row)
  #check selections
  common = set( fdeck[first-1] ).intersection( set(sdeck[second-1] ) )
  if len(common) == 0:
    print "Case #%d: Volunteer cheated!" % (n+1)
  elif len(common) == 1:
    print "Case #%d: %d" % (n+1, list(common)[0])
  else:
    print "Case #%d: Bad magician!" % (n+1)

