#! /usr/bin/env python2
fr=open("1a.in","r")
fw=open("1a.out","w+")
num_cases=int(fr.readline())
for case in range(1,num_cases+1):
	line=fr.readline()
	max,digits = line.split()
	max=int(max)
	digits = [int(d) for d in str(digits)]
	x=1
	no_of_claps=digits[0]
	no_of_invites=0
	while(x<max+1):
		if(no_of_claps>=x):
			no_of_claps=no_of_claps+digits[x]
			x+=1
		else:
			no_of_invites+=1
			no_of_claps+=1
	fw.write("Case #"+str(case)+": "+str(no_of_invites)+"\n")