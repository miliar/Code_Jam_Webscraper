



def bar(n, C, F, X):
	y = 0.0
	for i in range(0, n):
		y = y + C/(2.0 + i*F)
	return X/(2+n*F) + y, y

def bard(n, prev, C, F, X):
	return X/(2+n*F) + prev + C/(2+(n-1)*F), prev + C/(2+(n-1)*F)

def bs(begin, end, best, C, F, X):
	print "beg ", begin, " end ", end, " best ", best
	if (end - begin <= 1):
		return best
	mid = int(begin + (end - begin)/2)
	val = bar(mid, C, F, X)
	if (val < best):
		return bs(mid+1, end, val, C, F, X)
	else:
		return bs(begin, mid, best, C, F, X)
	

def foo() :
	f = open('D:/B-large.in', 'r')
	N = int(f.readline())
	for i in range(0, N):
		ll = f.readline().split()
		C = float(ll[0])
		F = float(ll[1])
		X = float(ll[2])

		prev, yp = bar(0, C, F, X)

		for j in range(1, int(X)):
			case, yp = bard(j, yp, C, F, X)
        		if (case < prev) :
				prev = case
			else:
				break
		if (prev < X/2):
			print "Case #"+str(i+1)+": "+str(prev)
		else:
			print "Case #"+str(i+1)+": "+str(X/2)
foo()
