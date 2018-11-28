import math

t = int(raw_input())
if t >=1 and t<=10000:
	for p in range(t):
		input = raw_input()
		n = int(input.split(' ')[0])
		k = int(input.split(' ')[1])
		if n>=1 and n<=30:
			if k>=0 and k<=100000000:
				if n==1:
					if k%2 ==0:
						status = 'OFF'
					else:
						status = 'ON'
				else:
					comp = pow(2,n)-1
					if k<comp:
						status = 'OFF'
					elif k==comp:
						status = 'ON'
					else:
						if (k-comp) % pow(2,n) == 0:
							status = 'ON'
						else:
							status = 'OFF'
				print 'Case #%d: %s' %(p+1,status)

