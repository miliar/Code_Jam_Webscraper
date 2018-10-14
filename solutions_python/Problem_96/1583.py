y=input()
for j in xrange(0,y):
#googlers=0
	l=raw_input()
	l=l.split()
	googlers=int(l[0])
	magiccases=int(l[1])
	target=int(l[2])
#	print 'target is' , int(target)
	x=[]
	for i in xrange(0,googlers):
		x.append(int(l[i+3]))
	count=0
	for i in xrange(0,googlers):
#x.append(input())
#		print 'x[i]/3' ,'is',str(x[i]/3)
		if(x[i]/3>=target):
#	print 'x[i]/3' is str(x[i]/3)
#			print 'count increases'
#			print 'should not come here'
			count+=1
		elif(x[i]/3<target):
#			print 'x[i]%3 is',str(x[i]%3)
#			print 'came to the target'
			if(x[i]%3==0):
#		print str(x[i]),'comes from',str(0),'hello'
#				print 'x[i]/3-1' ,'is',str((x[i]/3))
				if(magiccases!=0):
					if(((x[i]/3)+1)==target and x[i]!=0):
#						print 'count increases'
						count+=1
						magiccases-=1
			if(x[i]%3==1):
#				print str(x[i]-((x[i]/3)*2)),'comes from',str(1)
				if(x[i]-((x[i]/3)*2)==target):
#					print 'count increases'
					count+=1

			if(x[i]%3==2):
#				print str(x[i]),'comes from',str(2)
				if(magiccases!=0):
					if(x[i]-((x[i]/3)*2)==target):
#						print 'count increases'
						count+=1
						magiccases-=1
				if(x[i]-((x[i]/3)*2)>target):
#						print 'count increases'
						count+=1
		
						
	print 'Case','#'+str(j+1)+':',str(count)


