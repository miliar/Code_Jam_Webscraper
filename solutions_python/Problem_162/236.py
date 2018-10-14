

def rev(n):
	s = str(n)[::-1]
	s = s.lstrip('0')
	return eval(s)

cache = [-1]*1000001
for i in range(11):
		cache[i] = i
		
def solve_iter(n):
	
	for i in xrange(11, n+1):
		if i % 10 != 0 and rev(i) < i:
			cache[i] = 1 + min(cache[rev(i)], cache[i-1])
		else:
			cache[i] = 1 + cache[i-1]
#	print n, cache[n]
	return cache[n]	

solve_iter(1000000)
	
f = open("A-small-attempt1.in", 'r')
f2 = open("outputCountSmall.txt", 'w')	
t = int(f.readline())
for i in xrange(t):
	s = "Case #" + str(i+1) + ": "
	
	n = int(f.readline())
	print n, cache[n]
	if i == t-1:
		f2.write(s+str(cache[n]))
	else:
		f2.write(s+str(cache[n])+'\n')

f.close()
f2.close()
