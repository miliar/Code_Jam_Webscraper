import sys
from bisect import bisect_right


def find_le(a, x):
  'Find rightmost value less than or equal to x'
  #print x
  #print a
  i = bisect_right(a, x)
  if i:
    #print "Found"
    del a[i-1]
    return True
  return False

numCases = input()
for case in range( 1, numCases + 1 ):
  N, S = [ int(x) for x in raw_input().split() ]
  Nums = [ int(x) for x in raw_input().split() ]

  numDisks = 0

  SortedNums = sorted( Nums )

  while ( len( SortedNums ) > 0 ):
    largest = SortedNums.pop()
    #print largest
    numDisks += 1
    if ( len(SortedNums) > 0 ):
      #print SortedNums
      other = find_le(SortedNums, S - largest)
      #print SortedNums

  output = str( numDisks )
  print 'Case #' + str( case ) + ': ' + str( output )
