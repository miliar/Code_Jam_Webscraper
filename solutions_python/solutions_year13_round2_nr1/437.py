from math import *
t=raw_input()
t=int(t)
i=0

while i<t:
	l=[]
	ll=[]
	val=raw_input()
	val=val.split()
	v=int(val[0])
	n=int(val[1])
	s=raw_input()
	if v==1:
		mini= n
	
	else:
		s=s.split()
		j=0
		while(j<n):
			s[j]=int(s[j])
			j=j+1
		s.sort()
		k=0
		rk=0
		mini=n
		for j in s:
			if v>j:
				v+=j
			else:
				r=int(log((j-1)/(v-1),2)+1)
				v=j+(2**r)*(v-1)+1
				
				rk=rk+r
			ll.append(rk-k+n-1)
			if mini > ll[k]:
				mini=ll[k]
			#print v, r,j, mini
			k+=1
	ans="Case #"+str(i+1)+":"
	print ans,mini
	i=i+1
