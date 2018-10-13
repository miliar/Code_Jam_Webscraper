import sys

def istidy(n):
	s = str(n)
	return all(s[i] <= s[i+1] for i in xrange(len(s)-1))

def brute(n):
	while not istidy(n):
		n -= 1
	return n

def run(n):
	s = [0] + map(int, str(n))
	i = 0
	while i < (len(s)-1) and s[i] <= s[i+1]:
		i += 1

	if i == len(s) - 1:
		return n

	assert s[i] > s[i+1]

	m = s[i]-1
	bad = s[i]

	j = i
	while s[j] == bad and j > 0:
		s[j] = 9
		j -= 1
	
	s[j+1] = m

	assert j > 0 or s[j] == 0

	for k in xrange(i+1,len(s)):
		s[k] = 9

	return int(''.join(map(str,s)))

def smoke():
	import random

	for k in xrange(1000):
		n = random.randint(100000,999999)
		a = brute(n)
		b = run(n)
		print "%d: %d <-> %d" % (n,a,b)
		assert a == b

if __name__ == '__main__':
	#smoke()
	#sys.exit(0)

	T = int(raw_input())
	for t in xrange(T):
		n = int(raw_input())
		print "Case #%d: %s" % (t+1, run(n))
		#print "Case #%d: %s" % (t+1, brute(n))
