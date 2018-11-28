import sys

try: 
	f = open(sys.argv[1])
	out = open(sys.argv[1].rpartition("\\")[2]+".out", 'w')

	numTests = int(f.readline())

	for i in range (0, numTests):
		a1 = int(f.readline())

		for j in range (0,4):
			if j == a1-1:
				poss1 = f.readline()[0:-1].split(" ")
			else:
				f.readline()

		a2 = int(f.readline())

		for k in range (0,4):
			if k == a2-1:
				poss2 = f.readline()[0:-1].split(" ")
			else:
				f.readline()

		tot = 0
		chosen = -1
		for l in range(0,4):
			if poss1[l] in poss2:
				chosen = poss1[l]
				tot +=1
		
		if tot == 0:
			out.write("Case #" +str(i+1)+": Volunteer cheated!\n")
		elif tot > 1:
			out.write("Case #" +str(i+1)+": Bad magician!\n")
		else:
			out.write("Case #" +str(i+1)+": " +str(chosen)+"\n")


except IOError, e:
	print "Error %d: %s"%(e.args[0], e.args[1])

