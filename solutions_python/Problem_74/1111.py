count=int(raw_input())
for iter in xrange(count):
	nextOrder=[]
	queue=[[],[]]
	pos=[1,1]
	totalmoves=0
	string=raw_input()
	arr=string.split(' ')
	del arr[0]
	#print arr
	current,other=-1,-1
	even=1
	nextPos=-1
	for i in arr:
		if(even):
			nextOrder.append(i)
			if(i=='O'):nextPos=0
			else: nextPos=1
			even=0
		else:
			queue[nextPos].append(int(i))
			even=1
	#print queue[0]
	#print queue[1]
	for i in xrange(len(nextOrder)):
		trail=nextOrder[0]
		currepos,otherpos=-1,-1
		del nextOrder[0]
		if(trail=='O'):
			current=0
			other=1
		else:
			current=1
			other=0
		if(len(queue[current])):
			currentpos=queue[current][0]
		else:
	#		print "HECK THAT"
			currentpos=pos[current]
		if(len(queue[other])):
			otherpos=queue[other][0]
		else:	
			otherpos=pos[other]
		diff=abs(currentpos-pos[current])+1
		totalmoves+=diff
		pos[current]=currentpos
		del queue[current][0]
		mdiff=abs(pos[other]-otherpos)
		if(diff<mdiff):
			mdiff=diff
		if(pos[other]<otherpos):
			pos[other]+=mdiff
		else:
			pos[other]-=mdiff
	print "Case #"+str(iter+1)+": "+str(totalmoves)
				
