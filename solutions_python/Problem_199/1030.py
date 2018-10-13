from timeit import default_timer as timer

def flips(s, k):
	count = 0
	x = [int(a=='+') for a in s]
#	print s, k, x
	for i in xrange(len(s)-k+1):
		if x[i] == 0:
#			print 'Before: ', i, x
			for j in xrange(k):
				x[i+j] = (x[i+j] + 1) % 2
			count = count + 1
#			print 'After: ', x

	if x == [1]*len(s):
		return count
	else:
		return -1

start = timer()
filename = 'A-large'
f = open(filename + '.in', 'r')
g = open(filename + '.out', 'w')
t = int(f.readline())
for i in xrange(1, t+1):
	s, k = f.readline().split(' ')
	k = int(k)
	
	g.write('Case #' + str(i) + ': ')
	n = flips(s, k)
	if n == -1:
		g.write('IMPOSSIBLE\n')
	else:
		g.write(str(n) + '\n')
f.close()
g.close()
end = timer()
print (end - start)
