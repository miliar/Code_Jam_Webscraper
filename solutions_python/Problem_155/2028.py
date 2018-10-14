import sys

numCases = input()
for case in range( 1, numCases + 1 ):
  ( sMax, sList ) = raw_input().split()
  numStanding = 0
  numFriends = 0
  
  for x in xrange(0,len(sList)):
    s = int(sList[x])
    if s > 0 and numStanding < x:
      numNeeded = ( x - numStanding )
      numStanding += numNeeded
      numFriends += numNeeded
    
    numStanding += s
  
  output = numFriends

  print 'Case #' + str( case ) + ': ' + str( output )
