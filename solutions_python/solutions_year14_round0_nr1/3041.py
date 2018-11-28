#-------------------------------------------------------------------------------
# Name:        Magic Trick
# Purpose:
# Author:      newHorizons
#
# Created:     04/11/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys

# Global Variables

def main():

  # Define file objects
  fo_input = open( "A-small-attempt2.in", "r" )
  fo_output = open( "output.txt", "w" )

  # Get the number of test cases
  testCases = int( fo_input.readline().rstrip() )
  for testCase in range( testCases ) :
    # Inittializations
    arr1 = []
    arr2 = []
    # Get row for first query
    row1 = int(  fo_input.readline().rstrip() )
    # print ( "Query 1:", row1 )
    # Get set up of cards for first arrangement
    for row in range( 4 ) :
      # Get string from standard input
      testCaseStr = fo_input.readline().rstrip()
      # Split string to get row1 for first arrangement
      arr1.append( set( testCaseStr.split() ) )
    # for row in range( 4 ) : print ( arr1[row] )
    # Get row for second query
    row2 = int( fo_input.readline().rstrip() )
    # print ( "Query 2:", row2 )
    # Get set up of cards for second arrangement
    for row in range( 4 ) :
      # Get string from standard input
      testCaseStr = fo_input.readline().rstrip()
      # Split string to get row1 for second arrangement
      arr2.append( set( testCaseStr.split() ) )
    # for row in range( 4 ) : print ( arr2[row] )
    # first query for first arrangement and
    # second query for second arrangement
    # print( "Intersection of", arr1[row1-1], "and", arr2[row2-1] )
    prefixStr = "Case #" + str( testCase + 1 ) + ":"
    intersect = arr1[row1-1] & arr2[row2-1]
    # print( "Intersection:", intersect )
    if len( intersect ) == 0 :
      fo_output.write( prefixStr + " Volunteer cheated!\n" )
    elif len( intersect ) == 1 :
      fo_output.write( prefixStr + " " + intersect.pop() + "\n" )
    else :
      fo_output.write( prefixStr + " Bad Magician!\n" )

  fo_input.close()
  fo_output.close()

if __name__ == '__main__':
  main()