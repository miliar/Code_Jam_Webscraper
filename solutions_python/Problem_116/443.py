#!/usr/bin/env python


# Indicates the winner of a tic-tac-toe-tomek game based on the given game board
# Input:
#    board - a 4-element list of strings representing a 4x4 board
#          - each string has 4 characters and represents the pieces on a row
#            of the game board
#          - each character of a string may be X, O, T (wildcard) or . (vacant)
# Return Value: the winner for the game
#    - "X": player X won
#    - "O": player O won
#    - None: draw (neither player won)
#    - "": game is ongoing
def ticTacToeTomekWinner( board ):
   # Scan each row for a winner.
   for row in [ 0, 1, 2, 3 ]:
      piece = samePieceOnLine( board[ row ] )
      if piece in [ "X", "O" ]:
         return piece
   # Scan each column for a winner.
   for column in [ 0, 1, 2, 3 ]:
      # Form a list representing the pieces along the same column.
      line = ( board[ 0 ][ column ] + board[ 1 ][ column ] +
               board[ 2 ][ column ] + board[ 3 ][ column ] )
      piece = samePieceOnLine( line )
      if piece in [ "X", "O" ]:
         return piece
   # Check the negative slope diagonal for a winner.
   line = board[ 0 ][ 0 ] + board[ 1 ][ 1 ] + board[ 2 ][ 2 ] + board[ 3 ][ 3 ]
   piece = samePieceOnLine( line )
   if piece in [ "X", "O" ]:
      return piece
   # Check the positive slope diagonal for a winner.
   line = board[ 0 ][ 3 ] + board[ 1 ][ 2 ] + board[ 2 ][ 1 ] + board[ 3 ][ 0 ]
   piece = samePieceOnLine( line )
   if piece in [ "X", "O" ]:
      return piece
   # If this point is reached, it's either a draw or an ongoing game.
   # One or more vacant spaces indicates an ongoing game.
   if "." in ( board[ 0 ] + board[ 1 ] + board[ 2 ] + board[ 3 ] ):
      return ""  # ongoing game
   else:
      return None  # draw

# Indicates the type of piece on a given game board line if the line contains
# only one piece type
# Input:
#    line - a 4-element list
#         - each element may be X, O, T (wildcard) or . (vacant)
# Return Value: the piece type for the given game board line
#    - "X": all X (indicative of player X winning)
#    - "O": all O (indicative of player Y winning)
#    - ".": all vacant
#    - None: more than one type present on the given game board line
def samePieceOnLine( line ):
   # Determine the layout or layouts to check.
   if "T" in line:
      # If the wildcard piece is found in the given game board line, we create
      # 2 possible layouts. The first layout treats the wildcard piece like an
      # X while the second layout treats the wildcard piece like an O.
      layout1 = line.replace( "T", "X" )
      layout2 = line.replace( "T", "O" )
      layouts = [ layout1, layout2 ]
   else:
      # If the wildcard piece is not in the given game board line, we have only
      # one layout to check.
      layouts = [ line ]
   # Perform same piece checking on each layout.
   for layout in layouts:
      piece = layout[ 0 ]
      if ( ( layout[ 1 ] == piece ) and ( layout[ 2 ] == piece ) and
           ( layout[ 3 ] == piece ) ):
         return piece
   # Reaching this point indicates that the given game board line contains more
   # than one piece type.
   return None


# Main function
if __name__ == "__main__":
   # Get the number of test cases.
   T = int( raw_input() )
   for i in range( 0, T ):
      board = []
      for j in range( 0, 4 ):
         board.append( raw_input() )
      raw_input()  # account for the empty line after each test case
      winner = ticTacToeTomekWinner( board )
      if winner in [ "X", "O" ]:
         result = "%s won" % winner
      elif winner is not None:
         result = "Game has not completed"
      else:
         result = "Draw"
      print "Case #%d: %s" % ( i + 1, result )
