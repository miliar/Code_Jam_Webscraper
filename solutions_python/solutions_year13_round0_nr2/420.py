#!/usr/bin/env python


import copy


#
# Support Functions
#

# Determines the maximum value on a list
def maxAlongLine( line ):
   result = line[ 0 ]
   count = len( line )
   for i in range( 1, count ):
      if line[ i ] > result:
         result = line[ i ]
   return result

# Places on a single list the values of a given column in a 2-dimensional array
def columnValues( array2d, column ):
   result = []
   rows = len( array2d )
   for i in range( 0, rows ):
      result.append( array2d[ i ][ column ] )
   return result

# Indicates whether or not a desired lawn pattern is doable
def canDoPattern( array2d, rows, columns ):
   # Special Case: Any pattern on a 1-m wide or 1-m long lawn is always doable.
   if rows < 2 or columns < 2:
      return True
   # We obtain the maximum grass height along each row and column.
   rowMax = []
   for row in range( 0, rows ):
      rowMax.append( maxAlongLine( array2d[ row ] ) )
   columnMax = []
   for column in range( 0, columns ):
      columnMax.append( maxAlongLine( columnValues( array2d, column ) ) )
   # We iterate through each 1x1 meter square patch of lawn to see if the
   # desired height for the patch is doable. I realize that at worst case,
   # this solution is of the complexity order of O(N * M) but right now, I
   # don't have a more efficient algorithm in mind.
   for row in range( 0, rows ):
      for column in range( 0, columns ):
         height = array2d[ row ][ column ]
         # If the desired height is not the maximum along the row and also not
         # the maximum along the column, then there is no way to trim the patch
         # to the desired height without ruining the desired height of at least
         # one other patch along the same row or column. If we find even one
         # patch on the lawn that ruins the desired pattern, we have no choice
         # but to declare the desired pattern as undoable.
         if ( height < rowMax[ row ] ) and ( height < columnMax[ column ] ):
            return False
   # Reaching this point means that we found no patch that will cause the
   # desired pattern to be ruined. In this case, the desired pattern is doable.
   return True


#
# Main Function
#

if __name__ == "__main__":
   T = int( raw_input() )
   for i in range( 0, T ):
      line = raw_input()
      dimensions = line.split()
      N = int( dimensions[ 0 ] )
      M = int( dimensions[ 1 ] )
      lawn = []
      for row in range( 0, N ):
         currentColumn = []
         line = raw_input()
         heights = line.split()
         for column in range( 0, M ):
            currentColumn.append( int( heights[ column ] ) )
         lawn.append( copy.copy( currentColumn ) )
      if canDoPattern( lawn, N, M ):
         print "Case #%d: YES" % ( i + 1 )
      else:
         print "Case #%d: NO" % ( i + 1 )
