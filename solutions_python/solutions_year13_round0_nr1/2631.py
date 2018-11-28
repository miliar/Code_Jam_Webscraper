

def readBoard(file):
	board = [[0 for x in xrange(4)] for x in xrange(4)] 
	line=file.readline().replace('\n','')
	board[0]=line
	line=file.readline().replace('\n','')
	board[1]=line
	line=file.readline().replace('\n','')
	board[2]=line
	line=file.readline().replace('\n','')
	board[3]=line
	return board

def main():
	file=open('input.txt');
	size=file.readline()
	for i in range(0,int(size)):
		board=readBoard(file);
		res=checkBoard(board);
		if(res=="X" or res=="O"):
			print "Case #" + str(i+1) + ": " + res + " won"
		elif res=="DRAW":
			if(hasBlank(board)):
				print "Case #" + str(i+1) + ": Game has not completed"
			else:
				print "Case #" + str(i+1) + ": Draw"
		else:
			print "Case #" + str(i+1) + ": Game has not completed"
		file.readline()

def hasBlank(board):
	for line in board:
		if '.' in line:
			return True
	return False



def checkPos(board,pos):
	incomplete=False
	first_ind=pos[0]
	first=board[first_ind[0]][first_ind[1]]
	counter=1
	for x in pos[1:]:
		next=board[x[0]][x[1]]
		if(next=='.'):
			incomplete=True
			break;

		if(next=='T'):
			counter+=1
			continue;
			
		if(next==first):
			counter+=1
		else:
			break;
	
	if counter==4:
		return first

	if incomplete:
		return "incomplete"

	
	

def checkBoard(board):
	incomplete=False
	diag=[[0,0],[1,1],[2,2],[3,3]]
	diag2=[[0,3],[1,2],[2,1],[3,0]]
	cols = [[[x,y] for x in xrange(4)] for y in xrange(4)]
	rows = [[[y,x] for x in xrange(4)] for y in xrange(4)]
	poss= [diag] + [diag2] + cols + rows
	for pos in poss:
		a=checkPos(board,pos)
		if(a=="X" or a=="O"):
			return a
		elif a=="incomplete":
			incomplete=True

	if(incomplete):
		return "incomplete"

	return "DRAW"




main()	