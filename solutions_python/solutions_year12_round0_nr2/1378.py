import os

os.chdir("/Users/Junzologies/Dropbox/Code Jam/Qualification 2012/B")

filer=open("B-small-attempt3.in","r")
filew=open("B-small-attempt3.out","w")

cases=int(filer.readline())

for count in xrange(cases):
	line=filer.readline().split()
	n=int(line[0]) # no of googlers
	s=int(line[1]) # no of surprising
	p=int(line[2]) # best points
	googlers=line[3::] # googlers' points
	
	noHit=0
	noS=0
	
	for glr in googlers:
		glr=int(glr)			
		rpts=glr%3
		basic=glr/3
		diff=p-basic
		if rpts==0:
			if diff<=0: noHit+=1
			elif diff<=1:
				if noS<s and glr>=2:
					noHit+=1;noS+=1 
		elif rpts==1:
			if diff<=0: noHit+=1
			elif diff<=1: noHit+=1
			elif diff<=2:
				if noS<s and glr>=2:
					noHit+=1;noS+=1 
		elif rpts==2:
			if diff<=0: noHit+=1
			elif diff<=1: noHit+=1
			elif diff<=2:
				if noS<s and glr>=2:
					noHit+=1;noS+=1
	print count+1,googlers,noS,noHit
	filew.write("Case #"+str(count+1)+": "+str(noHit)+"\n")
filer.close()
filew.close()