import functools

def check(sumL, sumC, sumD, flag):
	#print(sumL, sumC, sumD, flag)
	if 4 in sumL or  4 in sumC or  4 in sumD or 8 in sumL or  8 in sumC or  8 in sumD:
		return 'X won'
	if 40 in sumL or 40 in sumC or 40 in sumD or 35 in sumL or  35 in sumC or  35 in sumD:
		return 'O won'
	if flag == False:
		return 'Game has not completed'
	else:
		return 'Draw'


f = open('A-large.in', 'rU')
o = open('A-large.out', 'w')
T = int(f.readline())
size = 4

for i in range(T):
	flag = True
	sumL = [0,0,0,0]
	sumC = [0,0,0,0]
	sumD = [0,0]
	board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for line in range(size):
		temp = f.readline().strip('\n')
		cnt = 0
		for c in temp:

			if c == 'X':
				board[line][cnt] = 1
				sumL[line] += 1
				sumC[cnt] += 1

			elif c == 'O':
				board[line][cnt] = 10
				sumL[line] += 10
				sumC[cnt] += 10
			
			elif c == 'T':
				board[line][cnt] = 5
				sumL[line] += 5
				sumC[cnt] += 5

			else:
				flag = False
			cnt += 1
		sumD[0] += board[line][line]
		#sumD[1] += board[line][*line+3]
	#sumD[0] = board[0][0] + board[1][1] + board[2][2] + board[3][3]
	sumD[1]	= board[0][3] + board[1][2] + board[2][1] + board[3][0]
	f.readline()
	#print(board,sumL,sumC, sumD)
	#print("Case #%d: %s" % (i+1,check(sumL, sumC, sumD, flag)))
	o.write("Case #%d: %s\n" % (i+1,check(sumL, sumC, sumD, flag)))
f.close()
o.close()
print("done!")