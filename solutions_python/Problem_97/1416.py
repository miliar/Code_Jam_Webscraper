import os

os.chdir("/Users/Junzologies/Dropbox/Code Jam/Qualification 2012/C")

filer=open("C-small-attempt0.in","r")
filew=open("C-small-attempt0.out","w")

cases=int(filer.readline())

for count in xrange(cases):
	line=filer.readline().split()
	A,B=int(line[0]),int(line[1])
	a,rpair=A,0
	
	while a<B:
		if a>9 and B>9: # more than 2 digits
			tA,b=str(a),B
			found=False
			while a<b:
				for d in xrange(len(tA)-1): # digit loop
					if tA[d+1::]+tA[0:d+1]==str(b):
						rpair+=1
						found=True
						break
				b-=1
			a+=1
		else:
			break
	filew.write("Case #"+str(count+1)+": "+str(rpair)+"\n")
	#print "Case #"+str(count+1)+": "+str(rpair)+"\n",
filer.close()
filew.close()