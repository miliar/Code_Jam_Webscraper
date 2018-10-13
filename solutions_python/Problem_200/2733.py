# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

def isNumberTidy(n):
	s = list(str(n))
	if s != sorted(s): return False
	return 'True'

def tidyNumbers(n):
	if isNumberTidy(n): return n
	i = 1
	while True:
		if isNumberTidy(n-i):
			return n - i
		i += 1

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n = int(raw_input())
		print "Case #{}:".format(i), tidyNumbers(n)
