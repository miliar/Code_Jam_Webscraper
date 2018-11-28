def parse_board():
	a = []
	for i in xrange(4):
		a.append(raw_input())
	raw_input()
	return a
	
def count_row(a,row,values):
	sum = 0
	for i in xrange(4):
		if a[row][i] in values:
			sum += 1
	return sum
	
def count_columns(a,col,values):
	sum = 0
	for i in xrange(4):
		if a[i][col] in values:
			sum += 1
	return sum
	
def count_diag(a,dir,values):
	sum = 0
	if dir == 0:
		for i in xrange(4):
			if a[i][i] in values:
				sum += 1
	else:
		for i in xrange(4):
			if a[i][-(i+1)] in values:
				sum += 1
	return sum
	
	
def check_win(a,player):
	values = ['T',player]
	for x in xrange(4):
		if count_row(a,x,values) == 4 or count_columns(a,x,values) == 4 or count_diag(a,x,values) == 4:
			return True
	return False
	
def check_finished(a):
	for x in xrange(4):
		if '.' in a[x]:
			return False
	return True
	
if __name__ == "__main__":
	trials = int(raw_input())
	file = open("output.txt",'w')
	
	for x in xrange(trials):
		a = parse_board()
		file.write("Case #%i: " % (x+1))
		if check_win(a,'X'):
			file.write("X won\n")
			continue
		elif check_win(a,'O'):
			file.write("O won\n")
			continue
		elif check_finished(a):
			file.write("Draw\n")
			continue
		else:
			file.write("Game has not completed\n")
			continue	
	file.close()
		