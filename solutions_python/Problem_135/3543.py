def common(l1,l2):
	l = []
	for i in range(0,len(l1)):
		if l1[i] in l2 and l1[i] not in l:
			l.append(l1[i])
	return l
fp = open('A-small-attempt1.in','r')
lines = fp.readlines()
for i in range(0,len(lines)):
	lines[i] = lines[i].strip()
	lines[i] = lines[i].split(' ')
t = int(lines[0][0])
lines = lines[1:]
fp.close()
fp = open('A-small-attempt1.out','w')
c = 1
while c<=t:
	t1 = int(lines[0][0])
	lines = lines[1:]
	l1 = lines[t1-1]
	lines = lines[4:]
	t2 = int(lines[0][0])
	lines = lines[1:]
	l2 = lines[t2-1]
	lines = lines[4:]
	temp = common(l1,l2)
	if len(temp)==1:
		fp.write("Case #"+str(c)+": "+temp[0]+"\n")
	elif len(temp)>1:
		fp.write("Case #"+str(c)+": Bad magician!\n")	
	else:
		fp.write("Case #"+str(c)+": Volunteer cheated!\n")	
	c = c+1
fp.close()
# end of program    

