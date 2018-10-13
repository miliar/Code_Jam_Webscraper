import math

for c in xrange(int(raw_input())):
	l = raw_input().split()
	token = int(l[1])
	n = int(l[2])
	googlers = map(int, l[3:])
	count = 0
	
	for g in googlers:
		r = g-n
		temp = r/2.
		a = int(temp)
		b = int(math.ceil(temp))
		#print a,b,n
		if n == 0:
			count +=1
		elif min(a, b) > n:
			count+=1
		elif (((abs(n-a) == 3) or (abs(n-b) == 3)) and (r >= 0 and a >= 0 and b >= 0)):
			pass
		elif (((abs(n-a) == 2) or (abs(n-b) == 2)) and (r  >= 0 and a  >= 0 and b  >= 0)):
			if token > 0:
				count+=1
				token-=1
		elif (((abs(n-a) == 1) or (abs(n-b) == 1))  and (r  >= 0 and a  >= 0 and b  >= 0)):
			count+=1
		elif (((abs(n-a) == 0) or (abs(n-b) == 0))  and (r  >= 0 and a  >= 0 and b  >= 0)):
			count+=1
	
	print "Case #"+str(c+1)+": "+str(count)
	