def pali(ari8):
	ari8=str(ari8)
	mik=len(ari8)
	first=0
	last=mik-1
	palindrome=True
	while ((last>first)and(palindrome==True)):
		if (ari8[first]!=ari8[last]):
			palindrome=False
		last=last-1
		first=first+1
	return palindrome

from math import sqrt

#filename=raw_input("insert filename in current directory>>")
filename="C-small-attempt1.in"
arch=open(filename,"r")
tcash=arch.readline()
tcash=int(tcash)

output=open("output1.txt","w")

#print "tcash=",tcash

for x in range(0,tcash):
	A,B=(arch.readline()).split()
	A=int(A)
	B=int(B)
	#print A,B
	start=int(sqrt(A))
	#print start
	count=0
	if (pali(start)and(pali(int(pow(start,2))))and(int(pow(start,2))>=A)):
		count=count+1
	start=start+1
	nummy=pow(start,2)
	while (nummy<=B):
		if((pali(start))and(pali(nummy))):
			count=count+1
		start=start+1
		nummy=int(pow(start,2))
	#print "Case #%d: %d"%(x+1,count)
	stp="Case #%d: %d\n"%(x+1,count)
	#print stp
	output.write(stp)
		

output.close()
arch.close()