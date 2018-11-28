input=open('input.txt','r');
output=open('output.txt','w');

firstline=True
linenumber=1
for newline in input:
	line=newline.split()
	highest=int(line[0])
	if firstline:
		firstline=False
		continue
	data=line[1]
	friends=0
	count=0
	i=0
	while i<=highest:
		s=int(data[i])
		if i>count+friends:
			friends+=i-(count+friends)
		count+=s
		i+=1
	output.write('Case #'+str(linenumber)+': '+str(friends)+'\n')
	linenumber+=1
input.close()
output.close()
