import sys


numCases = input()
for case in range( 1, numCases + 1 ):
  ( p, k ) = raw_input().split()
  k = int(k)
  p = list(p)
  flips = 0
  for i in xrange( 0, len( p ) - k + 1 ):
    if p[i] == '-':
      flips = flips + 1
      for j in xrange( i, i + k ):
        if p[j] == '-':
          p[j] = '+'
        else:
          p[j] = '-'
  
  output = flips
  if p.count('-') > 0:
    output = "Impossible"

  print 'Case #' + str( case ) + ': ' + str( output )
