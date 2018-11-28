
def compare(a,b):
	##print a,type(a),len(a)
	##print b,type(b),len(b)
	if(len(a[1]) == len(b[1])):
		if(a[1][0] > b[1][0]):
			return -1
		elif(a[1][0] < b[1][0]):
			return 1
		else:
			return 0
	else:
		return cmp(b[1],a[1])
cases = input()
for r1 in range(cases):
	n = input()
	servers = {}
	for i in range(n):
		s = raw_input()
		servers[s] = []
	q = input()
	qcount = 0
	for i in range(q):
		qcount += 1
		query = raw_input()
		servers[query] += [qcount]
	serverswitch = 0
	flag = 0
	while(True):
		items2 = servers.items()
		for i in items2:
			#print i[1],type(i[1])
			if(len(i[1]) == 0):
				flag = 1
				break
		if(flag ==1):
			print "Case #%d: %d"%(r1+1,serverswitch)
			break
		else:
			items2.sort(compare)
			#print items2
			newserver = {}
			#print servers
			for i in servers.keys():
				newserver[i] = []
			if(len(items2[0][1]) > 0):
				queueno = items2[0][1][0]
				servername = items2[0][0]
				for (server,calls) in servers.items():
					l1 = len(calls)
					for i in range(l1):
						if(calls[i] >= queueno):
							newserver[server] += [calls[i]]
				#print servers
				#print newserver
				servers = newserver
				#print servers
				serverswitch += 1


