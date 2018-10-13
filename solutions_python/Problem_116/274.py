from numpy import array,zeros

def valOf(char):
	if char=='X':
		return 1
	if char=='O':
		return -1
	if char=='T':
		return 100
	if char=='.':
		return -100
		
def judge(board):
	A="X won"
	B="O won" 
	C="Draw" 
	D="Game has not completed"

	for row in xrange(4):
		s = board[row,:].sum()
		if s==4 or s==103:
			return A
		if s==-4 or s==97:
			return B
	
	for col in xrange(4):
		s = board[:,col].sum()
		if s==4 or s==103:
			return A
		if s==-4 or s==97:
			return B
	s1=board.diagonal().sum()
	if s1==4 or s1==103:
		return A
	if s1==-4 or s1==97:
		return B
	s1=board[0,3]+board[1,2]+board[2,1]+board[3,0]
	if s1==4 or s1==103:
		return A
	if s1==-4 or s1==97:
		return B
	
	ndone = (-100 in board)
	if (ndone):
		return D
	else:
		return C
	
	
	
if __name__ == '__main__':

	f = open('A-large.in', 'r')
	num_samples = int(f.readline())

	for i in range(num_samples):
		board = zeros ((4,4))
		for row in xrange(4):
			line = f.readline().replace(' ','')
			for index in xrange(4):
				board[row,index] = valOf(line[index])

		print "Case #" + str(i+1) + ": "+ judge(board)
		f.readline()