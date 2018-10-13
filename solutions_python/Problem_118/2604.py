import gmpy2

def count(a,b):
	count = 0
	if gmpy2.is_square(a):
		start = gmpy2.isqrt(a)
	else:
		start = gmpy2.isqrt(a)+1
	
	start=long(start)
	end = long(gmpy2.isqrt(b))+1
	
	for i in range(start, end):
		j = i ** 2
		if (i == long(str(i)[::-1]) and j == long(str(j)[::-1])):
			count=count + 1
	
	return count

	

	
f = open('C-small-attempt0.in', 'r')
itr= int(f.readline().strip())

for inum in range(1,itr+1):
	x,y=map(int,f.readline().strip().split())
	fns=count(x,y)
	print "Case #"+ str(inum) + ": " +str(fns)
