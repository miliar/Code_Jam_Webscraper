
def graph(N, R, Y, B):

	if R*Y==0 and Y*B==0 and B*R==0:
		return ['IMPOSSIBLE']
	elif R*Y*B==0 and R!=Y and Y!=B and B!=R:
		return ['IMPOSSIBLE']

	stable = []

	if R==max([R, Y, B]):
		stable.append('R')
		R -= 1
	elif Y==max([R, Y, B]):
		stable.append('Y')
		Y -= 1
	else:
		stable.append('B')
		B -= 1

	for i in xrange(1, N-2):

		if R*Y==0 and Y*B==0 and B*R==0:
			return ['IMPOSSIBLE']
		elif R*Y*B==0:
			if R==0:
				if max(Y, B)-min(Y, B)>1:
					return ['IMPOSSIBLE']
				else:
					if Y==B and stable[0]==stable[-1]:
						return ['IMPOSSIBLE']
			if Y==0:
				if max(R, B)-min(R, B)>1:
					return ['IMPOSSIBLE']
				else:
					if R==B and stable[0]==stable[-1]:
						return ['IMPOSSIBLE']
			if B==0:
				if max(Y, R)-min(Y, R)>1:
					return ['IMPOSSIBLE']
				else:
					if Y==R and stable[0]==stable[-1]:
						return ['IMPOSSIBLE']
		
		if stable[-1]=='R':
			if Y>=B:
				stable.append('Y')
				Y -= 1
			else:
				stable.append('B')
				B -= 1
		elif stable[-1]=='Y':
			if R>=B:
				stable.append('R')
				R -= 1
			else:
				stable.append('B')
				B -= 1
		else:
			if Y>=R:
				stable.append('Y')
				Y -= 1
			else:
				stable.append('R')
				R -= 1

	if R==0 and Y==1 and B==1:
		if stable[0]!='B' and stable[-1]!='Y':
			stable.append('Y')
			stable.append('B')
		elif stable[0]!='Y' and stable[-1]!='B':
			stable.append('B')
			stable.append('Y')
		else:
			return ['IMPOSSIBLE']
	elif R==1 and Y==0 and B==1:
		if stable[0]!='R' and stable[-1]!='B':
			stable.append('B')
			stable.append('R')
		elif stable[0]!='B' and stable[-1]!='R':
			stable.append('R')
			stable.append('B')
		else:
			return ['IMPOSSIBLE']
	elif R==1 and Y==1 and B==0:
		if stable[0]!='R' and stable[-1]!='Y':
			stable.append('Y')
			stable.append('R')
		elif stable[0]!='Y' and stable[-1]!='R':
			stable.append('R')
			stable.append('Y')
		else:
			return ['IMPOSSIBLE']
	else:
		return ['IMPOSSIBLE']

	return stable
		


def main():
	T = int(raw_input())

	for t in xrange(T):

		line = raw_input().split()
		N, R, O, Y, G, B, V = map(int, line)
		

		print 'Case #'+str(t+1)+': '+''.join(graph(N, R, Y, B))


main()