filename = 'A-large.in'
f = open(filename,'r')

def ff(a,s):
	l = [a[0]=='-'] + [False]*(len(a)-s)
	q = [1 if a[0]=='-' else 0] + [0] * (len(a)-s)
	for i in range(1,len(a)-s+1):
		q[i] = sum(l[max(0,i-s+1):i])
		l[i] = (1 if a[i]=='-' else 0) != q[i]%2
	return l

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t ,
	a,s = f.readline().split()
	s = int(s)
	ans = ff(a,s)
	if ans[::-1] != ff(a[::-1],s):
		print "IMPOSSIBLE"
	else:
		ps = ''.join(['-' if sum(ans[max(i-s+1,0):min(len(a)-s+1,i+1)]) % 2 else '+' for i in range(len(a))])
		if ps == a:
			print (sum(ans))
		else:
			print "IMPOSSIBLE"