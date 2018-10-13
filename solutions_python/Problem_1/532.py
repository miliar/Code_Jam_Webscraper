import sys

outfile = open("qual.txt", "w")
infile = open("A-large.in", "r")

num_cases = int(infile.readline())

for i in range(1, num_cases + 1):
	print "Case #%s:\n" % i
	data = {}
	queries = []
	switches = 0
	printed = 0
	num_engines = int(infile.readline())
	
	for j in range(0, num_engines):
		data[infile.readline().rstrip("\n")] = [-1, -1]
	num_queries = int(infile.readline())
	for k in range(0, num_queries):
			query = infile.readline().rstrip("\n")
			queries.append(query)
			if data[query][0] != -1:
				data[query][1] = k
				continue
			data[query] = [k, k]

	data_sorted = sorted(data.iteritems(), key=lambda (k,v): (v,k))
	
	if data_sorted[0][1][0] == -1:
		outfile.write("Case #%s: 0\n" % i)
		printed = 1
		continue
		
	start = data_sorted[-1][1][0]
	engine = data_sorted[-1][0]
	pos = start
	q = start
	print start, engine, queries
	while q < num_queries:
		switched = 0
		temp = data.keys()
		temp.remove(engine)
		#print engine
		for s in queries[q+1:]:
			if temp.count(s) == 1:
				temp.remove(s)
				pos = pos + 1
				switched = 1
				engine = s
				if len(temp) == 0:
					break
			elif temp.count(s) == 0:
				pos = pos + 1
				continue
			else:
				break
		if len(temp) > 0:
			switches = switches + 1
			break
		if switched == 1:
			switches = switches + 1
			q = pos
		else:
			q = q + 1
		print q, num_queries
	if printed == 0:
		outfile.write("Case #%s: %s\n" % (i, switches))
		
infile.close()
outfile.close()