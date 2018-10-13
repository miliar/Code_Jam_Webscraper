def better_max(l):
	if l:
		return max(l)
	else:
		return 0

def test(i, j, dic, m, n):
	left = better_max(dic[i][0:j])
	right = better_max(dic[i][j+1:])
	up = better_max( [ l[j] for l in dic[0:i] ] )
	down = better_max( [ l[j] for l in dic[i+1: ] ] )
	if ( dic[i][j] >= max([left, right]) ) or ( dic[i][j] >= max([up, down]) ) :
		return True
	return False

def judge_case(l, m, n):
	dic = []
	if m == 1 or n == 1:
		return True

	for i in range(0, m):
		dic.append( [ int(c) for c in l[i].split() ] )
	for i in range(0, m):
		for j in range(0, n):
			if not test(i, j, dic, m, n):
				return False
	return True

def judge_all(filename):
	f = open(filename)
	lines = f.readlines()
	f.close

	num = int(lines[0])	
	current_line = 2
	for i in range(0,num):
		m = int(lines[current_line - 1].split()[0])
		n = int(lines[current_line - 1].split()[1])
		result = judge_case(lines[current_line: current_line + m], m, n)
		if result:
			phrase = "YES"
		if not result:
			phrase = "NO"
		print "Case #" + str(i+1) + ": " + phrase
		current_line += m + 1
		

judge_all("B-large.in")