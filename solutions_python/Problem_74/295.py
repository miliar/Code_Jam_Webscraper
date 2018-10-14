import sys

n = 0

for line in sys.stdin:
	if n == 0:
		n = 1
		continue
	
	word = line.split()
	
	R = []
	P = []
	O = [1,0]
	B = [1,0]
	time = 0
	I = int(word[0])
	for x in range(I):
		R += [word[1+x*2]]
		P += [int(word[2+x*2])]
	
	for x in range(I):
		if R[x] == 'O':
			mintime = O[1] + (abs(P[x] - O[0]) + 1)
			time = max((time + 1), mintime)
			O = [P[x],time]
		else:
			mintime = B[1] + (abs(P[x] - B[0]) + 1)
			time = max((time + 1), mintime)
			B = [P[x],time]
		
	print "Case #" + str(n) + ": " + str(time)
	n += 1
