import sys

s = open( 'b1.in' )
test_count = int( s.readline() )

def search( current ):
  global n
  global m
  global malt_count
  # check result TODO
  check_satisfied( current, malt_count )
  if len( current ) == n:
    return

  # try no malt
  current.append( 0 )
  search( current )

  current.pop()
  current.append( 1 )
  malt_count += 1

  search( current )
  current.pop()
  malt_count -=1


def check_satisfied( current, malt_count ):
  global arr
  global arrlen
  global best_result
  global best_malt_count
  global relevant_flavour
  satisfied = set()
  # all flavours
  for f in xrange( 0, n ):
    # who is satisfied? - all customers 
    for pos in xrange(0, arrlen ):
      cust = arr[pos]
      if len( current ) > f and cust.has_key( f+1 ) and cust[ f+1 ] == current[f]:
        satisfied.add( pos )
    if len( satisfied ) == m:
      if malt_count < best_malt_count:
        best_malt_count = malt_count
        best_result = list( current )
        break # success

for test_current in xrange(1, test_count+1):
  # read stuff
  n = int( s.readline() ) # flavours
  m = int( s.readline() ) # customers
  relevant_flavour = set()
  arr = list()
  for c in xrange( 0, m ):
    cust = dict()
    line = s.readline().strip().split( " " )
    t = int( line[0] )
    for xy in xrange( 0, t ):
      flav = int( line[ 1 + xy*2 ] )
      malt = int( line[ 2 + xy*2 ] )
      cust[ flav ] = malt
      relevant_flavour.add( flav )
    arr.append( cust )

  arrlen = len( arr )
  best_result = None
  best_malt_count = 99999
  malt_count = 0
  search( list() )
  # each flav
  # finished test
  if best_result != None:
    if len( best_result ) < n:
      for c in xrange( len( best_result ), n ):
        best_result.append( 0 )
    for x in xrange(0,len(best_result)):
      best_result[ x ] = str( best_result[ x ] ) 
    str_result = " ".join( best_result )
    print "Case #%i: %s" % ( test_current, str_result )
  else:
    print "Case #%i: IMPOSSIBLE" % ( test_current )
