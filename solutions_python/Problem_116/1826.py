''' first quals problem '''
def xMatch(path):
	for i in range(4):
		if path[i] == "O":
			return False
		elif path[i] == ".":
			return False
	return True
	
def oMatch(path):
	for i in range(4):
		if path[i] == "X":
			return False
		if path[i] == ".":
			return False
	return True
	
def emptyCheck(mine):
	for i in mine:
		for j in range(4):
			if i[j] == ".":
				return "Game has not completed"
	return "Draw"

T = int(raw_input())
for x in range(T):
	A = raw_input()
	B = raw_input()
	C = raw_input()
	D = raw_input()
	if x < T-1:
		E = raw_input()
	answer = ""
	# check if empty places as you go
	# check diags
	diag1 = A[0]+B[1]+C[2]+D[3]
	diag2 = A[3]+B[2]+C[1]+D[0]
	checks = [diag1,diag2,A,B,C,D]
	for i in range(4):
		checks += [A[i]+B[i]+C[i]+D[i]]
	
	for i in checks:
		if xMatch(i):
			answer = "X won"
			break
		elif oMatch(i):
			answer = "O won"
			break
	if answer == "":
		answer = emptyCheck(checks)
			
	print "Case #"+str(x+1)+": "+answer
