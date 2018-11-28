
f = open('A-large.in', 'r')




cases = dict()

count = int(f.readline().strip())

def get_winner(line):

	if "T" in line:
		line = line.replace("T", "")

	if line == ("X" * len(line)):
		return "X"
	
	elif line == ("O" * len(line)):
		return "O"
	return None

def check_column(case):
	for k in range(4):
		a = ''.join([c[k] for c in case])
		winner = get_winner(a)
		if winner:
			return winner
	return None

def check_row(case):
	for c in case:
		winner = get_winner(c)
		if winner:
			return winner
	return None

def check_diagonnal(case):
	d1 = ''.join([case[i][i] for i in range(4)])
	winner = get_winner(d1)
	if winner:
		return winner
	d2 = ''.join([case[i][3 - i] for i in range(4)])
	winner = get_winner(d2)
	if winner:
		return winner
	return None


checks = [check_row, check_column, check_diagonnal]
def check_case(case):
	for c in checks:
		w = c(case)
		if w: 
			return w + " won"

	for l in case:
		if "." in l:
			return "Game has not completed"
	return "Draw"



for i in range(count):
	case = []
	for j in range(4):
		case.append(f.readline().strip())
	#print "Case #%d" % i, case
	print "Case #%d: %s" % ((i + 1), check_case(case))
	# read empty line
	f.readline()






