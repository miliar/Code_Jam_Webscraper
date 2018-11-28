#-------------------------------------------------------------------------------
# Name:        Standing Ovation
# Purpose:
# Author:      newHorizons
#
# Created:     04/10/2015
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys

# Global Variables

def main():

  # Define file objects
  fo_input = open( "A-large.in", "r" )
  fo_output = open( "output.txt", "w" )

  # Initializations
  testCase = 0

  # Get the number of test cases
  testCases = int( fo_input.readline().rstrip() )
  # print ( "Number of Test Cases", testCases )

  # Iterate thru the test cases
  for testCase in range( testCases ) :
    # Initialization
    testCase += 1
    # Get data for current test case
    shynessMax, audience = fo_input.readline().rstrip().split()

    # Output test data for debugging
    # print ( "Test Case", testCase, ": max -", shynessMax, ", audience:", audience )

    # Initialize number of people clapping so far, and
    # total number of friends that we have had to add
    clapping = 0
    totalFriends = 0

    # Iterate thru the list of audience counts for each shyness level
    for shynessLevel in range(int(shynessMax) + 1) :
      # Get the count of audience for the current shyness level
      shynessCount = int(audience[shynessLevel])
      # If the number of total people clapping so far lags the current
      # shyness level, add new friends to make up the difference
      if clapping < shynessLevel :
        newFriends = shynessLevel - clapping
        clapping += newFriends
        totalFriends += newFriends
      # Increase the total number of people clapping,
      # by the audience count at this shyness level
      clapping += shynessCount

    # Ouptut the results for this test case
    prefixStr = "Case #" + str( testCase ) + ": "
    fo_output.write( prefixStr + str( totalFriends ) + "\n" )

  # Close file objects
  fo_input.close()
  fo_output.close()

if __name__ == '__main__':
  main()