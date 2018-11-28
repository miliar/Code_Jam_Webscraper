fin = open('A-small.in', 'r');
fout = open('A-small.out', 'w');

def f(x, y):
    return str(r)

T = int(fin.readline());

for i in range(T):
	args = fin.readline().split(' ')
	
	N = int(args[0])
	A = int(args[1])
	B = int(args[2])
	C = int(args[3])
	D = int(args[4])
	X = int(args[5])
	Y = int(args[6])
	M = int(args[7])

	Trees = [(X, Y)]

	for j in range(N-1):
		X = (A*X + B) % M
		Y = (C*Y + D) % M
		Trees = [(X, Y)] + Trees

	r = 0

	for j in range(N):
		for h in range(j+1,N):
			for l in range(h+1,N):
				if (Trees[j][0] + Trees[h][0] + Trees[l][0]) % 3 == 0 and (Trees[j][1] + Trees[h][1] + Trees[l][1]) % 3 == 0:
					r = r + 1

	fout.write('Case #' + str(i + 1) + ': ' + str(r) + '\n')
