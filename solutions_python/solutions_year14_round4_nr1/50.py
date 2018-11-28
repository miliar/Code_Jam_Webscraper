import sys


def dp(items,cap):
	f = [[] for i in range(0,cap+1)]
	best = 0
	for i in range(0,cap+1):
		for j in range(0,len(items)):
			if (i-items[j]>=0) and (not (j in f[i-items[j]])):
				f[i] = f[i-items[j]][:]
				f[i].append(j)
		if len(f[i])>0:
			best = i
	return (best,f[best])
def solve(inname,outname):
	fin = open(inname,'r')
	fout = open(outname,'w')

	T = int(fin.readline())
	for t in range(0,T):
		line = fin.readline()
		tokens = line.split()
		N = int(tokens[0])
		X = int(tokens[1])
		count = 0
		line = fin.readline()
		tokens = line.split()
		S = [int(x) for x in tokens]
		S.sort()
		v = [True for i in S]
		
		i = len(S)-1
		while i>=0:
			if v[i]:
				v[i]=False
				j = i-1
				while j>=0 and (S[j]+S[i]>X or v[j]==False):
					
					j-=1
				if  (j>=0):
					v[j]=False
				count+=1
			i-=1
	
		fout.write("Case #%d: %d\n"%(t+1,count))	
	fin.close()
	fout.close()

if __name__ == "__main__":
	inname = sys.argv[1]
	outname = sys.argv[2]
	solve(inname,outname)
