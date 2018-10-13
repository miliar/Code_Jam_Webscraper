# lines = open('example')
lines = open('D-small-attempt0.in')
# lines = open('A-large.in')
t = int(lines.readline())
for case in range(t):
	case += 1
	n = int(lines.readline())
	mat = {}
	for i in range(n):
		line = lines.readline()
		for j in range(n):
			mat[i,j] = int(line[j])

	clusters = set()
	for i in range(n):
		cluster = {i}
		cluster_mach = set()
		new_elem = {i}
		while new_elem:
			cur_elem = set()
			for elem in new_elem:
				for j in range(n):
					if mat[elem,j] and j not in cluster_mach:
						cluster_mach.add(j)
						for k in range(n):
							if mat[k,j] and k not in cluster:
								cluster.add(k)
								cur_elem.add(k)
			new_elem = cur_elem
		clusters.add((tuple(cluster),tuple(cluster_mach)))
	for j in range(n):
		test = False
		for i in range(n):
			test = test or mat[i,j]
		if not test:
			clusters.add((tuple([]),(j,)))
	
	nclusters = []
	total_cost = 0
	for cluster in clusters:
		for i in cluster[0]:
			for j in cluster[1]:
				if not mat[i,j]: total_cost += 1
		ncluster = (len(cluster[0]),len(cluster[1]))
		nclusters.append(ncluster)
	nclusters = [ c for c in nclusters if c[0] != c[1]]
	cls = sorted(nclusters,key=lambda x:  x[0]*x[1])
	
# # 	print(cls)
	while cls:
		lcls = list(cls)
		mcls = cls[-1]
		total_cost -= mcls[0] * mcls[1]
		cls = cls[:-1]
		add_clusters = []
		ncls = []
		add_cls2 = []
		if mcls[0] > mcls[1]:
			test = True
			for c in cls:
				if c[0] < c[1] and test:
					add_clusters.append(c)
					mcls = (c[0] + mcls[0] , c[1] + mcls[1])
					if mcls[1] >= mcls[0]:
						test = False
				else:
					ncls.append(c)
			for c in reversed(add_clusters):
				if mcls[1] - c[1] > mcls[0]:
					mcls = (c[0] - mcls[0] , c[1] - mcls[1])
					ncls.append(c)
				else :
					add_cls2.append(c)
		else:
			test = True
			for c in cls:
				if c[1] < c[0] and test:
					add_clusters.append(c)
					mcls = (c[0] + mcls[0] , c[1] + mcls[1])
					if mcls[0] >= mcls[1]:
						test = False
				else:
					ncls.append(c)
			for c in reversed(add_clusters):
				if mcls[1] - c[0] > mcls[1]:
					mcls = (c[0] - mcls[0] , c[1] - mcls[1])
					ncls.append(c)
				else :
					add_cls2.append(c)

		total_cost += mcls[0] *mcls[1]
		for c in add_cls2:
			total_cost -= c[0] * c[1]
		if mcls[0] != mcls[1]:
			ncls.append(mcls)
		cls = sorted(ncls,key=lambda x:  x[0]*x[1])
# 		print(lcls,cls)
		if len(cls) == len(lcls):
			break

	print ('Case #%d: %s'%(case,total_cost))
