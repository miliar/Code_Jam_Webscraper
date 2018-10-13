import sys
import re

def same_symbols(l,s):
	for i in range(len(l)):
		if l[i] != 'T' and l[i] != s:
			return False
		#end if
	#end for
	return True
	
def player_won(s,b):
	
	won = False
	# check diagonals	
	d1 = [b[0][0],b[1][1],b[2][2],b[3][3]]
	won = won or same_symbols(d1,s) 
	d2 = [b[0][3],b[1][2],b[2][1],b[3][0]]
	won = won or same_symbols(d2,s) 
	
	# check rows
	for r in range(4):
		won = won or same_symbols(b[r],s)
	#end for
	
	# check cols
	c1 = [b[0][0],b[1][0], b[2][0], b[3][0]]
	won = won or same_symbols(c1,s)
	
	c2 = [b[0][1],b[1][1], b[2][1], b[3][1]]
	won = won or same_symbols(c2,s)
	
	c3 = [b[0][2],b[1][2], b[2][2], b[3][2]]
	won = won or same_symbols(c3,s)
	
	c4 = [b[0][3],b[1][3], b[2][3], b[3][3]]
	won = won or same_symbols(c4,s)
		
	return won

def game_status(b):

	if player_won('X',b):
		return 'X won'
	#end if
	if player_won('O',b):
		return 'O won'
	#end if
	
	# check if board is filled
	for r in range(4):
		if not re.search("\.",b[r]):
			return 'Draw'
		#end if
	#end for
	return 'Game has not completed'
		
		
def main(args):

	f = open(args[1])
	lines = f.readlines()
	f.close()
	
	if len(lines) == 0:
		exit(0)
	#end if
	
	t = int(lines[0])
	for i in range(t):
		board = [ 
			lines[i*5+1].rstrip('\n'), 
			lines[i*5+2].rstrip('\n'), 
			lines[i*5+3].rstrip('\n'), 
			lines[i*5+4].rstrip('\n')]
		print "Case #{0}: {1}".format(i+1, game_status(board))
	#end for


if __name__ == "__main__":

	main(sys.argv)
	#print is_square(int(sys.argv[1]))
	#print is_palindrome(int(sys.argv[1]))
	#print num_fair_and_square(int(sys.argv[1]),int(sys.argv[1]));
#end if