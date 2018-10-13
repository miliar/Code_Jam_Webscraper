import sys

def idmin(A):
	i = 0
	mini = 0
	while i<len(A):
		if (A[mini]>A[i]):
			mini = i
		i+=1
	return mini

def solve(inname,outname):
	fin = open(inname,'r')
	fout = open(outname,'w')

	T = int(fin.readline())
	for t in range(0,T):
		N = int(fin.readline())
		tokens = fin.readline().split()
		A = [int(x) for x in tokens]
		count=0
		for i in range(0,N):
			x = idmin(A)
			if abs(x-(len(A)-1))>x:
				count = count + x
			else:
				count = count + (len(A)-1-x)
			tmp_A = [A[j] for j in range(0,len(A)) if not (j==x)]
			A = tmp_A[:]
		fout.write("Case #%d: %d\n"%(t+1,count))
	fin.close()
	fout.close()

if __name__ == "__main__":
	inname = sys.argv[1]
	outname = sys.argv[2]
	solve(inname,outname)
