#-------------------------------------------------------------------------------
# Name:        Cookie Clicker Alpha
# Purpose:
# Author:      newHorizons
#
# Created:     04/12/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys

# Constants
DIGITS = 7

# Global Variables
initialCookiesPerSecond = 2

def main():
  global  cookiesToBuyFarm, cookiesToAddPerSecond, cookiesToWinGame, minTime

  # Define file objects
  # fo_input = open( "B-small-attempt0.in", "r" )
  fo_input = open( "data4.txt", "r" )
  fo_output = open( "output.txt", "w" )

  # Get the number of test cases
  testCases = int( fo_input.readline().rstrip() )
  for testCase in range( testCases ) :
    # Inittializations
    minTime = 0
    # Get data for current test case
    value1Str, value2Str, value3Str = fo_input.readline().rstrip().split()
    cookiesToBuyFarm = float( value1Str )
    cookiesToAddPerSecond = float( value2Str )
    cookiesToWinGame = float( value3Str )

    timeSoFar = 0.0
    oldRate = initialCookiesPerSecond
    newRate = oldRate + cookiesToAddPerSecond
    timeWithOldRate = timeSoFar + ( cookiesToWinGame / oldRate )
    minTime = timeWithOldRate
    timeWithNewRate = timeSoFar + ( cookiesToBuyFarm / oldRate ) + \
      ( cookiesToWinGame / newRate )
    while timeWithNewRate < timeWithOldRate :
      minTime = timeWithNewRate
      timeSoFar += cookiesToBuyFarm / oldRate
      oldRate = newRate
      newRate += cookiesToAddPerSecond
      timeWithOldRate = timeSoFar + ( cookiesToWinGame / oldRate )
      timeWithNewRate = timeSoFar + ( cookiesToBuyFarm / oldRate ) + \
        ( cookiesToWinGame / newRate )

    # print( "Case #" + str( testCase + 1 ) + ": %.7f" % round( minTime, DIGITS ) )
    fo_output.write( "Case #" + str( testCase + 1 ) + ": %.7f" % round( minTime, DIGITS ) + "\n" )

  # Close file objects
  fo_input.close()
  fo_output.close()

if __name__ == '__main__':
  main()