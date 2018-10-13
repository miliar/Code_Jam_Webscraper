import sys
n=int(sys.stdin.readline())
for i in range(0,n):
	A,B,K=map(int,(sys.stdin.readline()).split())
	l=range(0,A)
	m=range(0,B)
	s=range(0,K)
	count=0
	for j in range(0,A):
		for k in range(0,B):
			if(j&k in s):
				count=count+1
	print "Case #" + str(i+1) + ": "+ str(count)
