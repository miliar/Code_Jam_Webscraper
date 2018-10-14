import sys

def solve_dec(kan, nao):
	npt = 0
	kan.sort()
	nao.sort()
	#print kan
	#print nao
	for n in nao:
		if n > min(kan):
			kan.remove(min(kan))
			npt +=1
	return npt

def solve(kan, nao):
	kan.sort()
	nao.sort()
	npt= 0
	kpt = 0
	for n in nao:
		j=0
		#print n, " ",  
		while j<len(kan) and kan[j]<n:
			j+=1
		if j == len(kan):
			kan.remove(kan[0])
			npt +=1
		else:
			#print kan[j]
			kan.remove(kan[j])
			kpt +=1
	return npt


N = int(sys.stdin.readline().strip())
for t in range(N):
	#print "Problem", t+1
	line = sys.stdin.readline().strip()
	line = sys.stdin.readline().strip()
	nao = [float(v) for v in line.split(" ")]
	line = sys.stdin.readline().strip()
	kan = [float(v) for v in line.split(" ")]
	
	#print kan
	#print nao
	solve(list(kan), list(nao))
	#print kan, nao
	solve_dec(list(kan), list(nao))
	#print solve(0, 2, c ,f ,x)
	print "Case #{0}: {1} {2}".format(t+1, solve_dec(list(kan), list(nao)), solve(list(kan), list(nao)))
	#print "Case #{0}: {1:0.7f}".format(t+1, solve(0, 2, c ,f ,x))