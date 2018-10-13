fin = open('A-large.in', 'r')
fout = open('final.out', 'w')
T = int(fin.readline())
lines = fin.readlines()
for i in range(T):
	ops = lines[i].rstrip().split(' ')
	N = int(ops[0])
	O = 1
	B = 1
	Od = 0
	Bd = 0
	time = 0
	for j in range(N):
		P = int(ops[2+2*j])
		if ops[1+2*j] == 'O':
			Odd = max(abs(P-O)+1-Bd,1)
			Od += Odd
			time += Odd
			O = P
			Bd = 0
		if ops[1+2*j] == 'B':
			Bdd = max(abs(P-B)+1-Od,1)
			Bd += Bdd
			time += Bdd
			B = P
			Od = 0
	s = 'Case #' + str(i+1) + ': ' + str(time) + '\n'
	fout.write(s)
