import numpy as np
def mainFunc(sN):	
	for i in range(len(sN)-1,0,-1):
		if(sN[i]<sN[i-1]): 
			sN[i-1]-=1
			for j in range(len(sN)-1,i-1,-1):
				sN[j]=9				
	ret = map(str,sN)
	ret = int(''.join(ret))
	return str(ret)

def bnary(num, N):
	ret = ""
	for i in range(N):
		ret = ret + str(num%2)
		num = int(num/2)
	return ret
		
T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' +	mainFunc(map(int, list(P[0])))