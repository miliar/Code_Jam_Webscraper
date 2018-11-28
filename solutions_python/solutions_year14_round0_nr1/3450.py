fileR = 'A-small-attempt0.in'
f = open(fileR,'r')
l = f.readlines()

for i in range(0,len(l)):
	l[i] = l[i].strip()
	l[i] = l[i].split(' ')
	
def intersection(l1,l2):
	l = []
	for i in range(0,len(l1)):
		if l1[i] in l2 and l1[i] not in l:
			l.append(l1[i])
	return l

test = int(l[0][0])
l = l[1:]

f = open('A-small-attempt0.out','w')


count = 1
while count<=test:
	t1 = int(l[0][0])
	l = l[1:]
	l1 = l[t1-1]
	l = l[4:]
	t2 = int(l[0][0])
	l = l[1:]
	l2 = l[t2-1]
	l = l[4:]
	temp = intersection(l1,l2)
	if len(temp)==1:
		f.write("Case #"+str(count)+": "+temp[0]+"\n")
	elif len(temp)>1:
		f.write("Case #"+str(count)+": Bad magician!\n")	
	else:
		f.write("Case #"+str(count)+": Volunteer cheated!\n")	
	count = count+1
f.close()
		
# end of program    

