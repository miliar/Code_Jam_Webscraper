t = int(raw_input())
for i in xrange(1, t + 1):
	n = [s for s in raw_input()]
	for j in range(len(n)-1, -1, -1):
		if j > 0:
			digit = int(n[j])
			front_digit = int(n[j-1])
			if digit < front_digit:
				for k in range(j, len(n)):
					n[k] = '9'
				front_digit -= 1
				n[j-1] = str(front_digit)
	print "Case #{}: {}".format(i, int(''.join(n)))
																												   
																												  
