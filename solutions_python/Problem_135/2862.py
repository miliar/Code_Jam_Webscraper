f = open("A-small-attempt2.in","r")
line = f.readline().strip()

t = int(line)
w = open("Output.txt","w")
for i in range(1,t+1):
	guess1 = int(f.readline().strip())
	for line in range(1,5):
		if line == guess1:
			l = f.readline()
			con1 = [int(s) for s in l.split() if s.isdigit()]
		else:
			f.readline()
	guess2 = int(f.readline().strip())
	for line in range(1,5):
		if line == guess2:
			l = f.readline()
			con2 = [int(s) for s in l.split() if s.isdigit()]
		else:
			f.readline()
	''' begin guess '''
	count = 0
	for c1 in con1:
		if c1 in con2:
			result = c1
			count+=1
		else:
			'''not in con2'''
	if count == 1:
		w.write("Case #"+str(i)+": "+str(result)+"\n")
	elif count > 1:
		w.write("Case #"+str(i)+": Bad magician!\n")
	elif count == 0:
		w.write("Case #"+str(i)+": Volunteer cheated!\n")
w.close()
f.close()