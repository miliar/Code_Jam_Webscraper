#! python

def gcd(a, b):
	if a < b:
		t = a
		a = b
		b = t

	while a % b:	
		if a < b:
			t = a
			a = b
			b = t
		a = a % b
		
	return b
def get_divisor(n, mul):
	t = 1
	l = []
	while t*t <= n:
	  if n % t == 0:
	    l.append(t*mul)
	    l.append(n/t*mul)
	  t += 1
	l.sort()
	return l
	
def lcm(a, b, LIMIT):
  l = a / gcd(a, b) * b
  if l > LIMIT:
    return -1
  else:
    return l
    
f = open("input.txt", "r")
wf = open("output.txt", "w")
T = int(f.readline().strip())
for case in xrange(T):
	s = f.readline().strip().split(" ")
	N = int(s[0])
	L = int(s[1])
	H = int(s[2])
	
	s = f.readline().strip().split(" ")
	for i in xrange(N):
	  s[i] = int(s[i])
	s.sort()
	
	gcds = [0] * (N+1)
	lcms = [0] * (N+1)
	gcds[N-1] = s[N-1]
	lcms[0] = s[0]
	for i in xrange(N-2, -1, -1):
	  gcds[i] = gcd(gcds[i+1], s[i])
	for i in xrange(1, N):
		if lcms[i-1] == -1:
			lcms[i] = -1
		else:
			lcms[i] = lcm(lcms[i-1], s[i], H)
			
	ans = -1
	
	for i in xrange(1, N):
	  if lcms[i-1] == -1:
	    continue
	  if gcds[i] >= lcms[i-1] and gcds[i] % lcms[i-1] == 0:
	    div = get_divisor(gcds[i]/lcms[i-1], lcms[i-1])
	    print " -- ", div
	    for item in div:
				if item > H: break
				if item < L: continue
				if (ans == -1 or ans > item):
					ans = item
				break
	  else:
	    continue
	
	print gcds
	print lcms
	g = gcds[0];
	div = get_divisor(g, 1)
	print div
	for item in div:
		if item > H: break
		if item < L: continue
		if (ans == -1 or ans > item):
			ans = item
		break
	l = lcms[N-1]
	if l != -1:
		nl = L / l * l
		if nl < L: nl += l
		if nl <= H and (ans == -1 or ans > nl):
			ans = nl
		
	if ans == -1:
		wf.write("Case #%d: NO\n"%(case+1))
	else:
		wf.write("Case #%d: %d\n"%(case+1, ans))

wf.close()