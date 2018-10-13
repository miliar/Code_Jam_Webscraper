import sys
# get the largest tidy number
def largestTidy(input, k):
	if validTidy(input):
		return input
		#Here to do the input file
	newNum = (input/10**k - 1) * 10**k + (10**k-1)
	return largestTidy(newNum, k+1)


# Get the valid tidy number
def validTidy(num):
	if num<10:
		return True
	return (num%10 >= (num/10)%10) and validTidy(num/10)


# here start the main program
if __name__=='__main__':
	cases = -1
	cnt = 1
	file = sys.argv[1]

	# open the file and call the largest tidy number and valid tidy number
	with open(file) as fin:
		for line in fin:
			if cases == -1:
				cases = line
			else:
				res = largestTidy(long(line), 1)
				print 'Case #%d: %s' % (cnt, res)
				cnt += 1
