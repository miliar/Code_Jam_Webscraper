def findFlip(p, k):
	l = len(p)
	a = [ c for c in p ]
	r = 0
	for i in range(l - k + 1):
		if a[i] == '-':
			# flip
			r += 1
			for j in range(i, i + k):
				a[j] = '+' if a[j] == '-' else '-'
		# print a
	for i in range(l):
		if a[i] == '-':
			return 'IMPOSSIBLE'
	return str(r)

# starts here
import sys
l = sys.stdin.readline()
count = int(l)

# results = []
for i in range(count):
	p, k = sys.stdin.readline().split()
	result = findFlip(p, int(k))

# print results
# for i in range(count):
	print 'Case #' + str(i+1) + ": " + result
