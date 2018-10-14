
def be(r,t):

	c = 0
	while True:

		nr = r+1
		a = nr**2 - r**2
		t-=a

		if t < 0:
			break
		else:
			c+=1

		r = nr+1

	return c


n = raw_input()
n = int(n)
for i in range(n):
	l = raw_input()
	toks = l.split()
	r = int(toks[0])
	t = int(toks[1])
	print "Case #%d: %d" %(i+1, be(r,t))


