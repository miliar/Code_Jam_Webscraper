

def isTidy(n):
	remR = n % 10
	n = n / 10
	while(n > 0):
		remL = n % 10
		if(remR >= remL):
			n = n / 10
			remR = remL
		else:
			return False
	return True
	
def main(n):
	while(n > 0):
		if(isTidy(n)):
			return n
		else:
			n = n - 1

if __name__ == '__main__':
	nCase = input()	# number of test cases
	for i in range(1, nCase + 1):
		n = input()		# get case value
		print "Case #%d: %d" % (i, main(n))
