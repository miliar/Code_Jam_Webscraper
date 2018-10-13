O = '1'
I = 'i'
J = 'j'
K = 'k'

MULT={O:{},I:{},J:{},K:{}}
MULT[O][O] = O
MULT[O][I] = I
MULT[O][J] = J
MULT[O][K] = K
MULT[I][O] = I
MULT[I][I] = O
MULT[I][J] = K
MULT[I][K] = J
MULT[J][O] = J
MULT[J][I] = K
MULT[J][J] = O
MULT[J][K] = I
MULT[K][O] = K
MULT[K][I] = J
MULT[K][J] = I
MULT[K][K] = O

SIGN={O:{},I:{},J:{},K:{}}
SIGN[O][O] = 1
SIGN[O][I] = 1
SIGN[O][J] = 1
SIGN[O][K] = 1
SIGN[I][O] = 1
SIGN[I][I] = -1
SIGN[I][J] = 1
SIGN[I][K] = -1
SIGN[J][O] = 1
SIGN[J][I] = -1
SIGN[J][J] = -1
SIGN[J][K] = 1
SIGN[K][O] = 1
SIGN[K][I] = 1
SIGN[K][J] = -1
SIGN[K][K] = -1

def check(s, x):
	'''Input string is s repeated x times'''
	ns = len(s)
	N = ns*x

	mi = O
	si = 1


	K_ind = set()
	mk = O
	sk = 1
	for k in range(N-1,1,-1):
		ck = s[k%ns]
		sk *= SIGN[ck][mk]
		mk = MULT[ck][mk]
		if mk==K and sk==1:
			K_ind.add(k)

	for i in range(N-2):
		ci = s[i%ns]
		si *= SIGN[mi][ci]
		mi = MULT[mi][ci]
		if mi != I or si != 1:
			continue
		mj = O
		sj = 1
		for j in range(i+1, N-1):
			cj = s[j%ns]
			sj *= SIGN[mj][cj]
			mj = MULT[mj][cj]
			if mj == J and sj == 1 and j+1 in K_ind:
				return True
	return False

def solve(testid):
	f = open(testid + '.in')
	g = open(testid + '.out', 'w')

	T = int(f.readline())

	for i in range(1,T+1):
		print i
		x = int(f.readline().split()[1])
		s = f.readline().strip()
		if check(s, x):
			result = "YES"
		else:
			result = "NO"

		g.write('Case #{}: {}\n'.format(i, result))

	f.close()
	g.close()

if __name__ == '__main__':
#	solve('C-sample')
	solve('C-small-attempt0')
#	solve('C-large')





