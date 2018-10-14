import math

t = int(raw_input())
for ti in xrange(t):
	n, k = map(int, raw_input().split())

	# starts creating the even odd matrix
	# even = []
	# odd = []

	# if (n%2==0):
	# 	even.append(1)
	# 	odd.append(0)
	# else:
	# 	even.append(0)
	# 	odd.append(1)

	# x = int(math.log(n,2))
	# for i in xrange(1,x+1):
	# 	odd.append(even[i-1])
	# 	even.append(int(math.pow(2,i)) - odd[i])
	# #this creates the even odd matrix completed

	x = int(math.log(k,2))
	p = int(math.pow(2,x))

	upper = n/p
	lower = upper -1

	count = (n-p+1-lower*p)/(upper-lower)

	ptr = k - (p - 1)

	val = upper if (ptr<=count) else lower
	#print val,upper,lower,count,ptr
	if (val%2==0):
		print "Case #"+str(ti+1)+": "+str(val/2)+" "+str(val/2-1)
	else:
		print "Case #"+str(ti+1)+": "+str(val/2)+" "+str(val/2)