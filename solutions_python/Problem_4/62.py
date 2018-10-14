import sys

s = open( 'A-large.in' )
test_count = int( s.readline() )

for test_current in xrange(1, test_count+1):
  # read stuff
  count = int( s.readline() )
  xst = s.readline().strip().split( " " )
  yst = s.readline().strip().split( " " )

  xs = list()
  ys = list()

  for x in xst:
    xs.append( int( x ) )

  for y in yst:
    ys.append( int( y ) )


  xs.sort()
  ys.sort()

  sum = 0
  pos = 0
  for x in xs:
    sum += ( x * ys[ count - pos - 1] )
    pos += 1

  # finished test
  print "Case #%i: %i" % ( test_current, sum )
