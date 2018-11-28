import sys

cin = sys.stdin.readline

def get_row(mylist, index):
	return mylist[index]

def get_column(mylist,index):
	a = []
	for i in xrange(4):
		a.append(mylist[i][index])
	return a

def get_diagonal1(mylist):
	a = []
	for i in xrange(4):
		a.append(mylist[i][i])
	return a

def get_diagonal2(mylist):
	a = []
	for i in xrange(4):
		a.append(mylist[i][3-i])
	return a

def decide_winner(mylist):
	a = []
	for i in xrange(4):
		a.append(get_row(mylist, i))
		a.append(get_column(mylist, i))
	a.append(get_diagonal1(mylist))
	a.append(get_diagonal2(mylist))
	for x in a:
		if (x.count('X') == 4) or ((x.count('X')) == 3 and ('T' in x)):
			return "X won"
		if (x.count('O') == 4) or ((x.count('O')) == 3 and ('T' in x)):
			return "O won"
	for x in a:
		if '.' in x:
			return "Game has not completed"

	return "Draw"

if __name__ == '__main__':
	f = open('b.txt', 'w')
	T = int(cin())
	for cnum in xrange(T):
			mylist = []
			for i in xrange(4):
				lin = list(cin().strip())
				mylist.append(lin)

			f.write("Case #{0}: {1}\n".format(cnum+1, decide_winner(mylist)))
			linebreak = cin()
	f.close()
