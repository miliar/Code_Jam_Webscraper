f1 = open('A-large.in','r')
f2 = open('output.in','w')
case = 0
inp = f1.readline()
input = int(inp)
for i in range(input):
	a = f1.readline()
	case = case + 1
	s = a.split()
	q = str(s[1])
	length = int(s[0])
	length+=1
	count = 0
	friends = 0
	#print q
	#print length
	for j in range(length):
		#print "In loop"
		if(count<j):
			#print count , j
			friends =friends + j - count
			count = count +1#
			#print friends
		if(q[j]>0):
			count = count + int(q[j])
		
	f2.write("Case #"+str(case)+": "+str(friends)+"\n")
	#print count, friends
f1.close()
f2.close()