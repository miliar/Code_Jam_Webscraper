import sys


def gcd(a,b):
	if(a > b):
		return gcd(b,a)
	if(a==0):
		return b
	else:
		return gcd(b%a,a)


count = 0
data = sys.stdin.readline()
T = int(data)
for omg in range(0,T):
	svals = sys.stdin.readline()
	val = svals.split()
	N = int(val[0])
	ts = [0]*N
	for i in range(1,N+1):
		ts[i-1] = int(val[i])
	ts.sort()
	diff = [0]*(N-1)
	A = 0
	for i in range(0,N-1):
		diff[i] = ts[i+1]-ts[i]
		A = gcd(A,diff[i])
	if(A == 1):
		print("Case #"+str(omg+1)+": "+str(0))
	else:
		print("Case #"+str(omg+1)+": "+str((A-(ts[1]%A))%A))





