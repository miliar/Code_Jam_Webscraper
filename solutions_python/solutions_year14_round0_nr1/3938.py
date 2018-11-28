op = open('output.txt','w')

with open('A-small-attempt3.in','r') as ip:
	N = int(ip.readline())
	for k in xrange(N):
		data = [[],[]]
		no = [[],[]]
		for i in range(2):
			no[i] = int(ip.readline())
			for j in range(4):	data[i].append([int(n) for n in ip.readline().split(' ')])

		result = list(set.intersection(set(data[0][no[0]-1]),set(data[1][no[1]-1])))
		res = 	'Case #'+str(k+1)+': '+str(result[0]) if len(result)==1 else	('Case #'+str(k+1)+': Bad magician!' if len(result)>1 else 'Case #'+str(k+1)+': Volunteer cheated!')
		res = res+'\n'

		op.write(res)