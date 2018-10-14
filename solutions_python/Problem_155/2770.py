# Solution for question 1
f=open('large.in','r')
ofile=open('Output1.txt','w')
f.readline()
ind=0
for line in f:
	ind=ind+1;
	words=line.split()
	pattern=words[1]
	index=0
	standing=0
	new=0
	for index in range(0,len(pattern)):
		if(standing<index):
			if(int(pattern[index])>0):
				defa=(index-standing)
				new=new+defa
				standing=standing+defa
		standing=standing+int(pattern[index])	
	ofile.write("Case #"+str(ind)+": "+str(new)+"\n")





		
