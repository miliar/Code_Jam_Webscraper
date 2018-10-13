#!/usr/bin/python

rawfile="A-large.in"

linenum=0

hf=open(rawfile,'r');
for line in hf :
	ostep=[]
	bstep=[]
	cases=0;
	allstep=[]

	linenum+=1

	rawvalue=line.split(' ')
	cases=int(rawvalue[0])
	for i in range(cases) :
		allstep.append(rawvalue[i*2+1])
		if(rawvalue[i*2+1]=='O'):
			ostep.append(int(rawvalue[i*2+2]))
		elif(rawvalue[i*2+1]=='B'):	
			bstep.append(int(rawvalue[i*2+2]))


	opos=1
	bpos=1
	
	oidx=0
	bidx=0
	
	allidx=0
	
	push=0
	
	step=0
	
	while(allidx<cases):
		step+=1
		#print "Time# "+str(step)+" o:"+str(opos)+" b:"+str(bpos)
	
		if(oidx<len(ostep)):
			if(opos!=ostep[oidx]):
				#print "Move Orange "+str(opos)+" to "+str(ostep[oidx])
				if(opos<ostep[oidx]):
					opos+=1
				else:
					opos-=1
			else:
				#push
				if((push==0)and(allstep[allidx]=="O")):
					push=1
					oidx+=1
					allidx+=1
					#print "Push Orange "+str(opos) 
				
		if(bidx<len(bstep)):
			if(bpos!=bstep[bidx]):
				#print "Move Blue "+str(bpos)+" to "+str(bstep[bidx])
				if(bpos<bstep[bidx]):
					bpos+=1
				else:
					bpos-=1
			else:
				#push
				if((push==0)and(allstep[allidx]=="B")):
					push=1
					bidx+=1
					allidx+=1
					#print "Push Blue "+str(bpos) 
		
	
		if(push==1):
			push=0
	
	print "Case #"+str(linenum)+": "+str(step)
	
