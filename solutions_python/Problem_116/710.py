from sys import stdin

S = 4

def solve( g ):
   def win( p ):
      def checkLine( line ):
         return all( c == p or c == 'T' for c in line )
      def checkLines( lines ):
         return any( checkLine( line ) for line in lines )

      return checkLines( [g[0], g[1], g[2], g[3],
         [g[0][0], g[1][0], g[2][0], g[3][0]],
         [g[0][1], g[1][1], g[2][1], g[3][1]],
         [g[0][2], g[1][2], g[2][2], g[3][2]],
         [g[0][3], g[1][3], g[2][3], g[3][3]],
         [g[0][0], g[1][1], g[2][2], g[3][3]],
         [g[0][3], g[1][2], g[2][1], g[3][0]]] )

   def inProgress():
      for line in g:
         if any( c == '.' for c in line ):
            return True
      return False

   if win( 'X' ):
      return "X won"
   elif win( 'O' ):
      return "O won"
   elif inProgress():
      return "Game has not completed"
   else:
      return "Draw"

T = int( stdin.readline() )
for i in range(T):
   grid = []
   for j in range(S):
      grid.append( stdin.readline().strip() )

   # Blank line
   stdin.readline()

   print "Case #{}: {}".format( i+1, solve( grid ) )
