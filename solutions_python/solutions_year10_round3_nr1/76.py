import sys, os

filename = "A-large"
#filename = "test"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

T = int(reader.readline().rstrip())

caseno = 1
while caseno<=T:
	N = int(reader.readline().rstrip())
	L = []
	R = []
	for i in xrange(N):
		l,r = [int(x) for x in reader.readline().rstrip().split(' ')]
		L.append(l)
		R.append(r)
	
	for i in xrange(N):
		lmax = i
		for j in xrange(i,N):
			if L[j]>L[lmax]:
				lmax = j
		tl = L[i]
		L[i] = L[lmax]
		L[lmax] = tl
		tr = R[i]
		R[i] = R[lmax]
		R[lmax] = tr
	
	ret = 0
	
	for i in xrange(N):
		for j in xrange(i,N):
			if R[i] < R[j]:
				ret+=1
	
	writer.write("Case #%s: %d\n" % (str(caseno),ret))
	caseno+=1

writer.close()