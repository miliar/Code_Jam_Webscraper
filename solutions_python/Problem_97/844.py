
t = []

def main():
	count = input()

	for i in xrange(count):
		print 'Case #%s: %s' % (i + 1, solve(raw_input()))

def solve(inputs):
	inputs = map(int, inputs.split())
	A = inputs[0]
	B = inputs[1]

	s = 0

	"""
	global t
	t = []
    """

	for i in xrange(A, B):
		s += num_pair(i, B)

	"""
	print len(t)
	print len(set(t))
	for x in t:
		if t.count(x) > 1:
			print x
    """
    
	return s

def num_pair(i, B):

	nums = rot(i)

	"""
	global t
	pairs = [(i, x) for x in nums if i < x <= B]
	for x, y in pairs:
		if sorted(str(x)) != sorted(str(y)):
			print x, y
		if x >= y:
			print x, y
		if not (i <= x < y <= B):
			print x, y
		t.append((x, y))
	"""

	return len([x for x in nums if i < x <= B])

def rot(i):
	a = list(str(i))

	t = []
	for n in range(1, len(a)):
		digits = ''.join(a[n:] + a[:n])
		t.append(int(digits))

	return set(t)

main()
