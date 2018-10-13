def isTydy(a) :
	b=1
	while a>100 and b==1 :
		if a%10==0 :
			return(0)
		elif a%10>=(a//10)%10 :
			a=a//10
		else :
			b=0
	if b==1 :
		if a%10==0 :
			return(0)
		elif a%10>=(a//10)%10 :
			return(1)
		else :
			return(0)
	else :
		return(0)


fichier=open("B-small-attempt9.in","r")
output=open("output","w")
ligne =(int)(fichier.readline())
cnt=0
while cnt<ligne :
	cnt=cnt+1
	nligne=(int)(fichier.readline())

	while(isTydy(nligne)==0) :
		nligne=nligne-1
	output.write("Case #")
	output.write(str(cnt))
	output.write(": ")
	output.write(str(nligne))
	output.write("\n")