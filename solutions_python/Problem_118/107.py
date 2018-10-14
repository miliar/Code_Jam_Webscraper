li = []
def isPalin(n):
	s = str(n)
	t = str(s)[::-1]
	return s==t
	
def brute(s):
	if(len(s) >= 13):
		s = str(int(s))
		t = str(s)[::-1]
		n = int(s+t)
		m = int(s+t[1:])
		n *= n
		m *= m
		if isPalin(n):
			li.append(n)
		if isPalin(m):
			li.append(m)
			#print n
		return
	solve(s+'0')
	solve(s+'1')
	solve(s+'2')

def okay(s):
	n = int(s)
	n *= n
	if isPalin(n):
		li.append(n)
		return True
	return False

def solve(l):
	arr = []
	for s in l:
		a = len(s)
		if(a > 51):
			return
		x = a/2
		s = s[x::]
		t = s[::-1]
		if(a % 2 == 1):
			if okay(t+s):
				arr.append(t+s)
		else:
			if okay(t+'0'+s):
				arr.append(t+'0'+s)
			if okay(t+'1'+s):
				arr.append(t+'1'+s)
			if okay(t+'2'+s):
				arr.append(t+'2'+s)
	solve(arr)
	

def lowerBound( x, lo, hi):
    while lo < hi:
        mid = (lo+hi)/2
        midval = li[mid]
        if midval < x:
            lo = mid+1
        else: 
            hi = mid
    return hi
    
def upperBound( x, lo, hi):
    while lo < hi:
        mid = (lo+hi)/2
        midval = li[mid]
        if midval <= x:
            lo = mid+1
        else: 
            hi = mid
    return lo


li.append(1)
li.append(4)
li.append(9)	
solve(["1", "2"])
hi = len(li)
t = input()
for test in range(t):
	a, b = map(int, raw_input().split())
	posa = lowerBound(a, 0, hi)
	posb = upperBound(b, 0, hi)
	print "Case #%d: %d\n" % (test+1, posb - posa),


