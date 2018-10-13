import Queue
f = open("Bin.txt","r")
g = open("Bout.txt","w")
number = int(f.readline())
for i in xrange(1,number+1):
	k = int(f.readline())
	st = f.readline()
	l = st.split()
	d = []
	for item in l:
		d.append(int(item))
	mini = 1000000
	for j in xrange(1,10):
		times = 0
		q = d[:]
		for item in q:
			if item > j:
				q.append(item-j)
				times += 1
		if times+j < mini:
			mini = times+j
	g.write("Case #%d: %d\n" % (i,mini))
		

