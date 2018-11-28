inp = open("B-large.in")
outp = open("output-large.txt","w")

T=int(inp.readline())
i=0

while (i<T):
	line = inp.readline()
	seq = line.split(" ")
	C = int(seq[0])
	D = int(seq[C+1])
	N = int(seq[C+D+2])
	
	el = seq[C+D+3]
	invo = el[0]
	
	outp.write("Case #"+str(i+1)+": ")
	for j in range(1,N):
		jj=0
		while (jj<C and len(invo)>0):
			#print "? "+invo[-1]+"+"+el[j]+"=="+seq[jj+1][0:2]
			if (invo[-1]+el[j]==seq[jj+1][0:2] or el[j]+invo[-1]==seq[jj+1][0:2]):
				#print "ya"
				#print "Cast "+invo+" + "+el[j]+" = "+invo[0:-1]+seq[jj+1][2]
				invo=invo[0:-1]+seq[jj+1][2]
				iii=0
				while (iii<len(invo)):
					jjj=C+2
					while (jjj<D+C+2):
						if (invo[iii]+seq[jj+1][2]==seq[jjj] or seq[jj+1][2]+invo[iii]==seq[jjj]):
							#print "Burn1 "+invo+" : "+invo[iii]+"+"+seq[jj+1][2]
							jjj=D+C+3
							iii=len(invo)		
							invo=""
						jjj+=1
					iii+=1
				jj=C+3
			jj+=1
				
		if (jj<C+3):
			#print "no"
			iii=0
			while (iii<len(invo)):
				jjj=C+2
				while (jjj<D+C+2):
					if (invo[iii]+el[j]==seq[jjj] or el[j]+invo[iii]==seq[jjj]):
						#print "Burn2 "+invo+" : "+invo[iii]+"+"+el[j]
						jjj=D+C+3
						iii=len(invo)+2
						invo=""
					jjj+=1
				iii+=1
			if (iii<len(invo)+2):
				invo+=el[j]				
				#print "Just "+invo+"\n"
		
				
	outp.write("[")
	if (len(invo)>0):
		outp.write(invo[0])
		for j in range(1,len(invo)):
			outp.write(", "+invo[j])	
	outp.write("]\n")
	
	#print "Total "+invo+" !!!\n"
		
	i+=1
