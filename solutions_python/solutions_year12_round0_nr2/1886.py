#!/x/opt/pp/bin/python2.6
import string, os, sys, commands,subprocess
f=open("B-small-attempt0.in")
line=f.readline()
test_case=int(float(line))
i=1
out_line=""
while test_case>=i:
	test_line=f.readline()
	params=test_line.split()
	N=int(float(params[0]))
	S=int(float(params[1]))
	P=int(float(params[2]))
	count=0
	offset=3
	while N>0:
		t=int(float(params[offset]))
		offset=offset+1
		N=N-1
		P3=3*P
		if t>=P3:
			count=count+1
		else:
			if t==P3-1 or t==P3-2:
				count=count+1
			elif S>0 and t>=P and t==P3-4:
				count=count+1
				S=S-1
			elif S>0 and t>=P and t==P3-3:
				count=count+1
				S=S-1
	out_line=out_line+"Case #"+str(i)+": "+str(count)+"\n"
	i=i+1 
f.close()
fo=open("result.txt","w")
fo.write(out_line)
fo.close()
