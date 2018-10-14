

def gen_recycled(i,k,a,b,r):
	s = str(i)
	for j in range(1,k):
		t = int(s[j:k]+s[0:j])
		if i<t<=b:
			r.add((i,t))

def rec_num(a,b,c):
	rec = set()
	k = len(str(a))
	for i in range(a,b+1):
		gen_recycled(i,k,a,b,rec)
	print "Case #"+str(c)+": "+str(len(rec))	

fd = file("input.in")
c = 1
for i in fd.readlines()[1:]:
	l = i.split(' ')
	rec_num(int(l[0]),int(l[1]),c)
	c = c+1
fd.close()
