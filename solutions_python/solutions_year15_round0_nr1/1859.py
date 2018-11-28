f = open('a.in', 'r')
nTestCase = int(f.readline()[0:-1])
for i in range(0,nTestCase):
	l = f.readline()[0:-1].split(' ')
	smax=int(l[0])
	audience=l[1]
	countPersons=0
	numFriends=0
	for j in range(0,len(audience)):
		if countPersons<j:
			numFriends=numFriends+1
			countPersons=countPersons+1
		countPersons=countPersons+int(audience[j])
	print "Case #"+str(i+1)+": "+str(numFriends)


