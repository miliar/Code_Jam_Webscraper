import sys


def largestTidy(input, k):
	if validTidy(input):
		return input

	newNum = (input/10**k - 1) * 10**k + (10**k-1)
	return largestTidy(newNum, k+1)

def validTidy(num):
	if num<10:
		return True
	return (num%10 >= (num/10)%10) and validTidy(num/10)

if __name__=='__main__':
	cases = -1
	cnt = 1
	file = sys.argv[1]

	with open(file) as fin:
		for line in fin:
			if cases == -1:
				cases = line
			else:
				res = largestTidy(long(line), 1)
				print 'Case #%d: %s' % (cnt, res) 
				cnt += 1




