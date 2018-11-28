file = open('B.txt','r')
f2 = open('Bout.txt','w')
T=file.readline()
T=int(T)
for i in range (0,T):
	s=''
	j= i+1
	s= 'Case #'+str(j)+': '
	line=file.readline()
	pos= line.find(' ',0)
	a=line[0:pos]
	b=line[pos+1:len(line)-1]
	#print a+' '+str(len(a))
	#print b+' '+str(len(b))
	#s= s+ str(a)+' '+str(b)
	#s=s[0:len(s)-1]
	#print s
	a=int(a)
	b=int(b)
	#print str(a)+' '+str(b)
	count=0
	for num in range(a,b+1):
		num=str(num)
		d=[]
		if (len(num)==2):
			x=num[0]
			y=num[1]
			newnum=y+x
			check=newnum
			newnum=int(newnum)
			num=int(num)
			if ( (newnum<=b) and (newnum>=a)):
				if ((newnum-num)!=0):
					if (check[0]!='0'):
						count=count+1
						#print str(newnum)+' '+str(num)
			num=str(num)
		else:
			tmp=0
			ok=0
			for j in range(0,len(num)-1):
				#print 'AAAAAAAAAAAA'
				num=str(num)
				x=num[0:j+1]
				y=num[(j+1):(len(num))]
				newnum=y+x
				check=newnum
				newnum=int(newnum)
				num=int(num)
				for k in range(0,tmp):
					if (d[k]==newnum):	
						ok = 1
						break
				if ok==0:	
					tmp=tmp+1
					d.append(newnum)
					
					
				#print str(newnum)+' '+str(num)
				#print str(newnum)
				if ( (newnum<=b) and (newnum>=a)):
					if (newnum!=num):
						if (ok==0):
							if (check[0]!='0'):
								count=count+1
	s=s+ str(count/2)
	s=s+'\n'		
	f2.write(s)	

 	
