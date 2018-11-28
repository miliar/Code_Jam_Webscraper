f = open('A-small-attempt1.in')
out = open('output','w')
lines = f.readlines()
testcase = int(lines[0])
for i in range(testcase):
	r1 = int(lines[10*i+1])
	tab1 =lines[10*i+1+r1].rstrip('\n').split(' ')
	r2 = int(lines[10*i+6])
	tab2 = lines[10*i+6+r2].rstrip('\n').split(' ') 
	match = 0
	elem =''
	for x in range(4):
		for y in range(4):
			if tab1[x]==tab2[y]:
				match = match+1
				elem = tab1[x]
	if match == 0 : out.write("Case #%d: Volunteer cheated!\n"%(i+1)) 
	if match == 1 : out.write("Case #%d: %s\n"%(i+1, elem)) 
	if match > 1 : out.write("Case #%d: Bad magician!\n"%(i+1)) 
f.close()
out.close()