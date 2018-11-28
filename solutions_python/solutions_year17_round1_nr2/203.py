import math

def up(j,x):
	return int(j/(0.9*x))

def dn(j,x):
	return math.ceil(j/(1.1*x))

numruns = int(input())
for run in range(numruns):
	print('Case #{0}: '.format(run+1),end='')
	
	dat = input().split()
	N = int(dat[0])
	P = int(dat[1])
	
	need = [int(i) for i in input().split()]
	packages=[sorted([int(i) for i in input().split()]) for j in range(N)]
	kits=0
	index=[0]*N
	while max(index)<P:
		upper=10**7
		lower=-1
		for i in range(N):
			upper=min(upper,up(packages[i][index[i]],need[i]))
			lower=max(lower,dn(packages[i][index[i]],need[i]))
		if lower<=upper:
			kits+=1
			for i in range(N):
				index[i]+=1
		else:
			for i in range(N):
				if up(packages[i][index[i]],need[i])==upper:
					index[i]+=1
	print(kits)