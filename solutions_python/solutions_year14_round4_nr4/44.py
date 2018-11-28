import sys


def get_pref(S):
	lista = []
	for s in S:
		for i in range(0,len(s)+1):
			tmp = s[:i]
			if not (tmp in lista):
				lista.append(tmp)
	#print S
	#print len(lista)
	return len(lista)
		

def get_all(status,A,N):
	ct = 0
	for i in range(0,N):
		S = [A[j] for j in range(0,len(A)) if status[j]==i]
		ct = ct + get_pref(S)
	return ct

def fac(a,n):
	b = a
	i = n
	while i>1:
		b = (b * i) % 1000000007
		i = i - 1
	return b

def solve(inname,outname):
	fin = open(inname,'r')
	fout = open(outname,'w')

	T = int(fin.readline())
	for t in range(0,T):
		#print "CAAAAAASE"
		tokens = fin.readline().split()
		M = int(tokens[0])
		N  = int(tokens[1])
		A = []
		for i in range(0,M):
			A.append(fin.readline()[:-1])
			
	
		status = [0 for i in range(0,M)]
		
		i = 0
		best_sol = -1
		best_count = 0
		while i<M:
			i = 0
			while i<M and status[i]==N-1:
				i = i + 1
			if i<M:
				status[i]+=1
				for k in range(0,i):
					status[k]=0
				#print status
				sol = get_all(status,A,N)
				#print sol
				if sol==best_sol:
					best_count+=1
				elif sol>best_sol:
					best_count=1
					best_sol = sol
		#ans = sol*fac(best_count,N)
		ans = best_count
		if N==1:
			ans = get_pref(A)
			best_sol = ans
			ans = 1 
		fout.write("Case #%d: %d %d\n"%(t+1, best_sol,ans))	
	fin.close()
	fout.close()

if __name__ == "__main__":
	inname = sys.argv[1]
	outname = sys.argv[2]
	solve(inname,outname)
