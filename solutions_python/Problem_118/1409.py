import math
def odp(odp, test):
	print "Case #" +str(test) +": " + str(odp)
	
def czykwadrat(x):
	if math.sqrt(x)**2 > int((math.sqrt(x)))**2:
		return False
	else:
		return True
def czypalindrom(x):
	ss=str(x)
	ii=0
	ll=len(ss)-1
	jj=(ll+1)/2
	while ii<jj:
		if ss[ii]!=ss[ll-ii]:
			return False
		ii+=1
	return True
	
t=input()
i=0
while(i < t):
	j=0
	wynik=0
	line=raw_input()
	line=line.split()
	n=int(line[0])
	m=int(line[1])
	while (n<=m):
		if czypalindrom(n):
			if czykwadrat(n):
				if czypalindrom(int(math.sqrt(n))):
					wynik+=1
		n+=1
		
	odp(wynik, i+1)
	i=i+1
	
