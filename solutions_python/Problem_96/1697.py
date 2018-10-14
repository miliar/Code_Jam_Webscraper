def getTotal(s):
	return sum(s)
	
def getBest(s):
	return max(s)
	
def decompose(N):
	r = N%3
	x = N//3
	if r == 2:
		return (x+1, -1)
	else:
		return (x, r)

def process(tots, S, p):
	num = 0
	for tot in tots:
		if tot == 0:
			if p == 0:
				num += 1
			continue
		(x, r) = decompose(tot)
		if(x+1 < p):
			continue
		if(x >= p):
			num += 1
			continue
			
		# here x < p and x >= p-1, i.e. x = p-1
		if (r==1):
			num += 1
		elif S > 0:
			num += 1
			S -= 1
	return num
	
def run():
	fin = open('B-large.in', 'r')
	L = [[int(i) for i in x.strip().split()] for x in fin.readlines()]
	fin.close()
	
	T = L[0][0]
	fout = open('B.out', 'w')
	fout.writelines(['Case #' + str(i) + ': ' + str(process(L[i][3:], L[i][1], L[i][2]))+ '\n' for i in xrange(1, T+1)])
	fout.close()
		
run()
