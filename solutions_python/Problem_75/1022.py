f=open(r'smallinput_B.in', 'r')
n=f.readline()
n=n.rsplit( )[0]
n=int(n)
#  print n
for m in range(1, n+1):
	line = f.readline()
	line=line.rstrip("\n\r ")	
	line=line.split(' ')
	refC = {}
	refO = {}
	com = []
	opp = []
	c= int(line.pop(0))
	for i in range(1, c+1) :
		s=line.pop(0)
		refC[s[0]+s[1]] = s[-1]
	com = refC.keys()
		
	d = int(line.pop(0))
	for i in range(1, d+1) :
		t = line.pop(0)
		refO[t[0]] = t[1]
		refO[t[1]] = t[0]
	opp = refO.keys()
	#  print "com is ", com
	#  print "opp is ", opp
	n= int(line.pop(0))
	str = line.pop(0)
	#  print n, str
	list = []
	for i in range(0, n) :
		list.append(str[i])
	#  print list
	try :
		i=0
		while ( i < len(list)-1) :
			if 	(list[i]+list[i+1] in com) or (list[i+1]+list[i] in com) :
				#  print list[i]+list[i+1], "present in com"
				try : list[i] = refC[list[i]+list[i+1]]
				except KeyError : list[i] = refC[list[i+1]+list[i]]
				del list[i+1]
				#  print list
			elif (list[i+1] in opp) and  refO[list[i+1]] in list[0:i+1]:
				#  print list[i+1], "present in opp"
				del list[0:i+2]
				i=0
				#  print list
			
			else :
				#  print list
				i=i+1
		#  print "out of loop"
	except IndexError : 
		print '', #  print "job is done", list
	myString = ", ".join(list )
	print 'Case #{0}: [{1}]'.format(m, myString)