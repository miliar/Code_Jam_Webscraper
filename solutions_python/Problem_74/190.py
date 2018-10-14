import sys
def f(ii,first):
	s=first.split()[1:]
	
	rob=[]
	pos=[]
	
	for i in range(len(s)):
		if i%2==0:
			rob.append(s[i])
		else:
			pos.append(int(s[i]))

	pressed=[0]*len(pos)

	#print rob
	#print pos
	#print pressed

	x = 0

	currB=1
	currO=1

	while sum(pressed)!=len(pressed):
		x+=1
		bb=1
		oo=1
		to=0
		tb=0

		try:
			pb=rob.index("B")
			tb=pos[pb]
		except:
			bb=0


		try:
			po=rob.index("O")
			to=pos[po]
		except:
			oo=0
			
		if oo==0:
			po=pb+1
		if bb==0:
			pb=po+1

		
		if pb<po and currB==tb and bb==1:
			pressed[pb]=1
			rob[pb]="X"

		if po<pb and currO==to and oo==1:
			pressed[po]=1
			rob[po]="X"

		if tb<currB:
			currB-=1
		elif tb>currB:
			currB+=1

		if to<currO:
			currO-=1
		elif to>currO:
			currO+=1
		
		#print x, sum(pressed),len(pressed), currB, currO
	print "Case #"+str(ii)+": " + str(x)


#	for i in s:
#		posR=1
#		posO=1
	
#		for k in i[1:]:
#			next

		
		



b = open(sys.argv[1]).readlines()

for i in range(int(b[0])):
	f(i+1,b[i+1])


