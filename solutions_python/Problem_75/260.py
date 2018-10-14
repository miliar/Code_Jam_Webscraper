#!/usr/bin/python


fp = open('b.in')

fp.readline()
lc = 0

for line in fp:
	line = line[:-1]
	c = 0
	arr = line.split(' ')
	ct = int(arr[c])
	c = c + 1
	reaction = {}
	opp = {}
	
	while ct > 0:
		tmp = arr[c]
		reaction[tmp[0]+tmp[1]] = tmp[2]
		reaction[tmp[1]+tmp[0]] = tmp[2]
		ct = ct - 1
		c = c + 1
		
	
	ct = int(arr[c])
	c = c + 1	
	
	while ct > 0:
		tmp = arr[c]
		opp[tmp[0]] = tmp[1]
		opp[tmp[1]] = tmp[0]
		ct = ct - 1
		c = c + 1
	
	query = arr[c+1]
	
	ret = []
	
	i = 0
	while (i < len(query)):
		opposed = False
		ret.append(query[i])

		if len(ret) > 1 and ret[len(ret)-1]+ret[len(ret)-2] in reaction:
			tmp = reaction[ret[len(ret)-1]+ret[len(ret)-2]]
			ret = ret[:-2]
			ret.append(tmp)
		elif query[i] in opp and opp[query[i]] in ret:
			ret = []
					
		i = i + 1
	lc = lc + 1	
#	print opp, reaction, query
	print "Case #%d:" % (lc), str(ret).replace("'","")
