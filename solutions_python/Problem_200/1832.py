
def isTidy(numberdigits):
	for i in xrange(len(numberdigits)-1):
		if numberdigits[i]>numberdigits[i+1]:
			return True
	return False


t = int(raw_input())  # read a line with a single integer
for k in xrange(1, t + 1):
	N = int(raw_input())
	digits = [int(d) for d in str(N)]
	size = len(digits)
	finaldigits = digits
	while(isTidy(finaldigits)):
		digits = finaldigits
		finaldigits = []
		for i in xrange(len(digits)-1):
			if digits[i]>digits[i+1]:
				finaldigits.append(digits[i]-1)
				for x in xrange(0,size-i-1):
					finaldigits.append(9)
				break
			else:
				finaldigits.append(digits[i])
	num = 0
	for j in xrange(0,len(finaldigits)):
		num+=finaldigits[len(finaldigits)-j-1]*(10**j)
	# print num
	print "Case #{}: {}".format(k, num)
