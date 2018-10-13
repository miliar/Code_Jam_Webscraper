import sys

numCases = input()
for case in range( 1, numCases + 1 ):
  p = raw_input()
  p = list(p)
  output = ""
  nineIndex = -1
  for i in xrange( len( p ) - 1, 0, -1 ):
    c = int( p[i] )
    n = int( p[i-1] )
    if c < n:
      p[i-1] = str( int(p[i-1])-1 )
      nineIndex = i

  startIndex = 0
  for c in p:
    if c == '0':
      startIndex = startIndex + 1
    else:
      break

  if ( nineIndex < 0 ):
    output = ''.join( p )
  else:
    output = ''.join( p[startIndex:nineIndex] ) + ( '9' * ( len(p) - nineIndex ) )
  print 'Case #' + str( case ) + ': ' + str( output )
