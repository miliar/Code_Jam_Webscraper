import sys
def check(b, n, iscol) :
	count = dict()
	count['.'] = count['X'] = count['O'] = count['T'] = 0
	for i in range(4):
		if iscol == 0:
			count[b[n][i]] += 1
		elif iscol == 1:
			count[b[i][n]] += 1
		elif n % 2:
			count[b[i][i]] += 1
		else :
			count[b[i][3 - i]] += 1
	if (count['T'] + count['O'] == 4) or (count['O'] == 4):
		return 'O'
	elif (count['T'] + count['X'] == 4) or (count['X'] == 4):
		return 'X'
	elif count['.'] > 0:
		return '.'
	else: return 'D'
	
def get_status(b):
	is_full = True;
	for iscol in range(3):
		for n in range(4):
			s = check(b, n, iscol)
			if s == 'O' :
				return 'O won'
			elif s == 'X' :
				return 'X won'
			elif s == '.' :
				is_full = False;
	if is_full:
		return 'Draw'
	else :
		return 'Game has not completed'
			
cases = input()
for i in range(1, cases + 1):
	board = []
	for j in range(4):
		board.append(raw_input())
	print 'Case #%i: %s' % (i, get_status(board))
	#print board
	raw_input()

