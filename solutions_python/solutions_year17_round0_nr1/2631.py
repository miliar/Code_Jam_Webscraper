t = int(raw_input())

def is_up(ch):
	if ch == '+':
		return True
	return False

def flip(a):
	return not a

for i in xrange(t):
	s, k = raw_input().split(' ')
	s = map(is_up, list(s))
	k = int(k)
	step = 0

	for j in xrange(len(s) - k + 1):
		if not s[j]:
			step = step + 1
			s[j:j+k] = map(flip, s[j:j+k])

	if not all(s):
		step = "IMPOSSIBLE"

	print "Case #{}: {}".format(i+1, step)
