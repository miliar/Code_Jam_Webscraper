import sys
import math


file = open(sys.argv[1])
line = file.readline()
#line = '1'
T=int(line)
for X in range(1,T+1):
	line = file.readline()
	#line = '2'
	N = int(line)
	
	line = file.readline()
	#line = '0.7 0.2'
	tokens = line.split(" ")
	NB = []
	for token in tokens:
		NB.append(float(token))

	NB.sort()

	line = file.readline()
	#line = '0.8 0.3'
	tokens = line.split(" ")
	KB = []
	for token in tokens:
		KB.append(float(token))
	KB.sort()
	KBD = KB[:]
	
	fairwincount = 0
	cheatcount = 0
	for nc in NB:
		for kc in KB:
			if kc > nc:
				#NB.remove(nc)
				KB.remove(kc)
				break
		else:
			#NB.remove(nc)
			KB.remove(KB[0])
			fairwincount = fairwincount + 1;
		
		if nc < KBD[0]:
			KBD.remove(KBD[-1])
		else:
			KBD.remove(KBD[0])
			cheatcount = cheatcount + 1;


	print("Case #"+str(X)+": "+str(cheatcount)+" "+str(fairwincount))

