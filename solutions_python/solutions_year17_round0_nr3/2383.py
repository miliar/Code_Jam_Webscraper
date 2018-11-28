def powertwo(x):
	ans = 0
	for j in range(x,0,-1):
		if((j & (j-1)) == 0):	
			ans = j;
			break;
	return ans

import math

T = int(raw_input())

for i in range(T):
	N,K = raw_input().split()
	N = int(N)
	K = int(K)
	A = N - K		#empty spots
	if(K==1):
		B = A
	else:
		B = A / powertwo(K)

	if(B == 0):
		print 'Case #'+str(i+1)+': '+ '0' + ' ' + '0'
	elif(B%2 == 0):		
		print 'Case #'+str(i+1)+': '+ str(B/2) + ' ' + str(B/2)
	else:
		print 'Case #'+str(i+1)+': '+ str(B/2 + 1) + ' ' + str(B/2)