inf = open('C-large.in', 'r')
outf = open('candyAns.txt', 'w')

T = int(inf.readline())
for i in xrange(T):
	c = inf.readline()
	c = inf.readline()
	c = map(int, c.split())
	num = reduce(lambda x, y: x^y, c)
	if num == 0:
		sum = reduce(lambda x, y: x + y, c)
		ans = str(sum - min(c))
	else:
		ans = 'NO'
	outf.write('Case #' + str(i+1) + ': ' + ans + '\n')

inf.close()
outf.close()
		
