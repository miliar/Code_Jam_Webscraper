

f = open('A-small-attempt1.in','r')
w = open('answer.o','w')
amount = f.readline()[:-1]
c = 0
i = 0
vol1 = ''
vol2 = ''
l1 = [['a' for x in xrange(4)] for x in xrange(4)] 
l2 = [['a' for x in xrange(4)] for x in xrange(4)] 

def get_response():
	global l1,l2, vol1, vol2
	row1 = l1[int(vol1)-1]
	row2 = l2[int(vol2)-1]
	ans = []
	# print row1
	# print row2
	for r1 in row1:
		for r2 in row2:
			if r1 == r2:
				ans.append(r1)
	a = len(ans)
	if a == 1:
		return ans[0]
	if a == 0:
		return 'Volunteer cheated!'
	if a > 1:
		return 'Bad magician!'

for line in f:
	line = line[:-1]
	# print line
	if i == 0:
		vol1 = line
		# print 'vol1'
	elif i>0 and i<5:
		l1[i-1] = line.split(' ')
		# print 'l1['+(i-1)+']'
	elif i == 5:
		vol2 = line
		# print 'vol2'
	elif i>5:
		l2[i-6] = line.split(' ')
		if i == 9:
			i = -1
			c+=1
			if str(c) == amount:
				w.write('Case #'+str(c)+': '+get_response())
			else:
				w.write('Case #'+str(c)+': '+get_response()+'\n')
		# print 'l2['+(i-6)+']'

	i+=1

print 'done'