def conta(list, arg):
	ret =0
	for a in list:
		if(a==arg):
			ret =1
	return ret
def clea( arg ,twos):
	for two in twos:
		a=list(two)
		if (conta(arg,a[0])==1)&(conta(arg,a[1])):
			#print('y')
			arg=list('')
	return arg
def cmb( arg,trips):
	for trip in trips:
		a=list(trip)
		l = len(arg)
		if l>=2:
			#print('x')
			#print(arg[l-2]+arg[l-1]+'  '+a[0]+a[1])
			if (arg[l-2]==a[0])&(arg[l-1]==a[1]):
				#print('xb')
				arg.append(a[2])
				arg[l-2]='Rem1'
				arg[l-1]='Rem2'
				arg.remove('Rem1')
				arg.remove('Rem2')
			
			elif (arg[l-1]==a[0])&(arg[l-2]==a[1]):
				#print('xb')
				#print(arg)
				arg.append(a[2])
				arg[l-2]='Rem1'
				arg[l-1]='Rem2'
				arg.remove('Rem1')
				arg.remove('Rem2')
			else:
				d=5
	return arg	
	
f =open('B-small-practice.in')
m=open('out','w')
cases =int(f.readline())
for case in range(1,cases+1):
	line = f.readline().split()
	#print(line)
	C=int(line[0])
	 
	cnt=0
	trips=list('')
	twos=list('')
	for a in range(1,C+1):
		trips.append(line[a])
		cnt+=1
	cnt+=1
	#print(trips)
	D=int(line[cnt])
	 
	for b in range(1,D+1):
		twos.append(line[cnt+b])
		
		cnt+=1
	cnt+=1
	#print(twos)
	N=int(line[cnt])
	#print(N)
	cnt+=1
	data=line[cnt]
	#print(data)
	out=list('')
	temp=list('')
	for leta in data:
		out.append(leta)
		#print(out)
		out = cmb( out ,trips)
		out = clea( out ,twos)
		
	#print(out)
	print(("Case #"+str(case)+': '+str(out)).replace('\'',''))
	m.write(("Case #"+str(case)+': '+str(out)).replace('\'','')+'\n')