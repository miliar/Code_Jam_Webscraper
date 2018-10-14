import sys

inputFilePath 	= sys.argv[1]
outputFilePath 	= sys.argv[2]

PLAYER_1 	= 'O'
PLAYER_2 	= 'X'
DRAW		= 'Draw\n'
INCOMPLETE	= 'Game has not completed\n'

def solve(grid,player, checkFull = False) :
  '''
  grid 		: is an array of length 16
  player 	: 'O' or 'X'
  checkFull	: True <-> we should check to see if the grid if full.
  Returns a tupe (s,fg) where s is True <-> player has won the game
  and fg is True -> the grid is full (no '.'), False -> is the grid contains
  a '.' and None if we havent check for it.
  '''
  WAYS_TO_WIN	= [	# HORIZONTAL
			(0,1,2,3),
			(4,5,6,7),
			(8,9,10,11),
			(12,13,14,15),
			# VERTICAL
			(0,4,8,12),
			(1,5,9,13),
			(2,6,10,14),
			(3,7,11,15),
			# DIAGONAL
			(0,5,10,15),
			(3,6,9,12),
		  ]
  fullGrid = True
  
  def isMatch(v) :
    ''' Returns True <-> v matches the player val or 'T' '''
    return v in (player,'T')
  
  def isEmpty(v) :
    ''' Returns True <-> v matches an empty '''
    return v == '.'
  
  for i0,i1,i2,i3 in WAYS_TO_WIN :
    if isMatch(grid[i0]) and isMatch(grid[i1]) and isMatch(grid[i2]) and isMatch(grid[i3]) :
      return (True,None)
    elif checkFull and (isEmpty(grid[i0]) or isEmpty(grid[i1]) or isEmpty(grid[i2]) or isEmpty(grid[i3])) :
      fullGrid = False
  return (False,fullGrid)

def main() :   
  with open(inputFilePath) as fIn :
    with open(outputFilePath,'wb') as fOut :
      T	= int(fIn.next().strip())
      for t in xrange(T) :
	grid	= []
	for _ in xrange(4) :
	  grid.extend(list(fIn.next().strip()))
	res1,_	= solve(grid,PLAYER_1)
	outStr	= 'Case #%i: ' % (t+1)
	if res1 :
	  outStr += '%s won\n' % PLAYER_1
	  fOut.write(outStr)
	else :
	  res2,fg	= solve(grid,PLAYER_2,checkFull=True)
	  if res2 :
	    outStr += '%s won\n' % PLAYER_2
	  elif fg :
	    outStr += DRAW
	  else :
	    outStr += INCOMPLETE
	  fOut.write(outStr)
	if t < T-1 :
	  fIn.next()
	

if __name__ == '__main__' :
  main()
  