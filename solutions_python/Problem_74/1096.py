def press(arg):
	arg+=1
	return arg

f =open('A-large.in')
m=open('out','w')
cases =int(f.readline())
for case in range(1,cases+1):
	line = f.readline().split()
	print(line)
	N=int(line[0])
	inst=list('')
	for a in range(1,N*2,2):
		
		inst.append(line[a]+line[a+1])
	
	orangepos=1
	oftime=0
	bluepos=1
	bftime=0
	tottime=0
	print(inst)
	for i in inst:
		s=list(i)
		if(i[0]=='B'):
			#print('O')
			
			gpos=int((str(i[1:]).replace('\'','').replace(' ','').replace(',','').replace('[','').replace(']','')))
			dist=abs(gpos-bluepos)
			bluepos=gpos
			#print('b'+str(bluepos))
			#print('d'+' '+str(dist))
			#print(bftime)
			if(bftime>=dist):
				dist=0
				oftime+=1#pressing
			else:
				dist=dist-bftime
				oftime=oftime+1+dist#pressing
			tottime+=dist
			#print ('tb4p'+str(tottime))
			tottime=press(tottime)
			bftime=0
		elif(i[0]=='O'):
			#print('B')
			pos=int((str(i[1:]).replace('\'','').replace(' ','').replace(',','').replace('[','').replace(']','')))
			dist=abs(pos-orangepos)
			orangepos=pos
			#print ('o'+str(orangepos))
			#print('d'+' '+str(dist))
			#print(oftime)
			if(oftime>=dist):
				dist=0
				bftime+=1#pressing
			else:
				dist=dist-oftime
				bftime=bftime+1+dist#pressing
			tottime+=dist
			#print ('tb4p'+str(tottime))
			tottime=press(tottime)
			oftime=0
		else:
			g=0
	#print(tottime)
	print(("Case #"+str(case)+': '+str(tottime)))
	m.write(("Case #"+str(case)+': '+str(tottime))+'\n')