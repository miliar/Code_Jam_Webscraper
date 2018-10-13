import sys

def parse(filename):
	cases = []
	T = 0
	with open(filename,'r') as f:
		T = int(f.readline())
		for i in range(T):
			XRC = f.readline().split()
			X = int(XRC[0])
			R = int(XRC[1])
			C = int(XRC[2])
			cases.append((X,R,C))
	return T, cases

def get_result_as_string(i, yes):
	if yes:
		return "Case #%i: GABRIEL\n"%(i+1)
	return "Case #%i: RICHARD\n"%(i+1)

def get_result(X,R,C):
	if X==1:
		return True
	if X==2:
		if R*C%2==0:
			return True
		else:
			return False
	if X==3:
		if (R==3 and C>1) or (C==3 and R>1):
			return True
		else:
			return False
	if X==4:
		if (R==4 and C>2) or (C==4 and R>2):
			return True
		else:
			return False


if __name__ == "__main__":
	if len(sys.argv) > 1:
		T, cases = parse(sys.argv[1])
		with open('lolilol2.txt','w') as f:
			for i in range(T):
				yes = get_result(cases[i][0], cases[i][1], cases[i][2])
				print(get_result_as_string(i,yes)[:-1])
				f.write(get_result_as_string(i,yes))


