fin=open("A-large.in")

t=int(fin.readline())

for i in range(0, t):
	n,m =fin.readline().strip().split()
	n=int(n)
	m=int(m)
	paths = []
	newdirs = []
	for j in range(0, n):
		#paths.append(fin.readline().strip().split("/"))
		path = fin.readline().strip()
		path = path.split("/")
		r = "/"+path[1]
		for idx in range(2, len(path)):
			if r not in paths:
				paths.append(r)
			r=r+"/"+path[idx]
		paths.append(r)
		#paths.append(fin.readline().strip())
	for j in range(0, m):
		#newdirs.append(fin.readline().strip().split("/"))
		newdirs.append(fin.readline().strip())

	sum = 0;

	options = []
	for ndir in newdirs:
		#print ":",ndir
		options = []
		"""
		for j in paths:
			#print paths
			jpaths = j.split("/")
			jplen = len(jpaths)
			for k in range(0, jplen-1):
				npath = "/".join(jpaths[0:jplen-k])
				#print "Searching", npath, "in ", ndir
				if npath in ndir:
					if len(ndir)>len(npath):
						if ndir[len(npath)]=="/":
							options.append(npath)
					else:
						options.append(npath)
			#if(len(options)!=0):
				#break
		"""
		#print "Paths: ", paths
		ndirs = ndir.split("/")
		n="/"+ndirs[1]
		for idx in range(2, len(ndirs)):
			if n not in paths:
				paths.append(n)
				sum+=1
				#print sum
			#print n
			n=n+"/"+ndirs[idx]
		if n not in paths:
			sum+=1
			#print sum
			#print n
			paths.append(n)
		#root = ""

		#for j in options:
		#	if len(j)>len(root):
		#		root = j
		#print options
		#print ndir, root
		#parentc = len(ndir.split("/"))
		#rootc = len(root.split("/"))
		#ndirs = ndir.split("/")
		#nd = ndirs[0]
		#for idx in range(1, len(ndirs)):
		#	if nd not in paths:
		#		paths.append(nd)
		#	nd=nd+"/"+ndirs[idx]
		


		#sum=sum+(parentc-rootc)
		#print sum

	print "Case #%d: %d" % ((i+1),sum)

	




