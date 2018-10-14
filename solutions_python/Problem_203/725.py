from timeit import default_timer as timer

start = timer()
filename = 'A-large'
f = open(filename + '.in', 'r')
g = open(filename + '.out', 'w')
t = int(f.readline())
for k in xrange(1, t+1):
	r, c = [int(x) for x in f.readline().split(' ')]
	cake = []
	for i in xrange(r):
		cake.append(f.readline())
	cake_ar = [['' for i in xrange(c)] for j in xrange(r)]
	for i in xrange(r):
		for j in xrange(c):
			cake_ar[i][j] = cake[i][j]
			
	for i in xrange(r):
		for j in xrange(c):
			if cake[i][j] != '?':
				letter = cake[i][j]
				r1 = i
				r2 = i
				c1 = j
				c2 = j
				while c1 > 0 and cake_ar[i][c1-1] == '?':
					cake_ar[i][c1-1] = letter
					c1 = c1-1
				while c2 < c-1 and cake_ar[i][c2+1] == '?':
					cake_ar[i][c2+1] = letter
					c2 = c2 + 1
				while r1 > 0 and cake_ar[r1-1][c1:c2+1] == ['?']*(c2-c1+1):
					cake_ar[r1-1][c1:c2+1] = [letter]*(c2-c1+1)
					r1 = r1 - 1
				while r2 < r-1 and cake_ar[r2+1][c1:c2+1] == ['?']*(c2-c1+1):
					cake_ar[r2+1][c1:c2+1] = [letter]*(c2-c1+1)
					r2 = r2 + 1
				#print r1, r2, c1, c2, cake_ar

	
	g.write('Case #' + str(k) + ': ' + '\n')
	for i in xrange(r):
		for j in xrange(c):
			g.write(cake_ar[i][j])
		g.write('\n')

f.close()
g.close()
end = timer()
print (end - start)
