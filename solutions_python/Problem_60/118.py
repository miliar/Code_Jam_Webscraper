inFile="/home/se/Downloads/B-large.in"

input = open(inFile)
output = open("/home/se/Downloads/test.out", "w")

line = input.readline().strip()
cases = int(line)

for case in range (0, cases):
	line = input.readline().strip()
	fields=line.split(" ")
	N=int(fields[0])
	K=int(fields[1])
	B=int(fields[2])
	T=int(fields[3])

	chickens = []
	line = input.readline().strip()
	loc=line.split(" ")
	line = input.readline().strip()
	speed=line.split(" ")
	
	for chick in range (0,N):
		v = int(speed[chick])
		x = int(loc[chick])
		chickens.append([B-x, v, (float((B-x))/v)])
	
	chickens.sort(key=lambda chick: chick[0])
	
	k = 0
	ahead = 0
	swaps = 0
	through = {}
	
	for chick in chickens:
		if chick[2] <= T:
			k+=1
			swaps+=ahead
		else:	
			ahead+=1
			
		if k==K:
			break
			
	if k==K:	
		print >> output, "Case #%d: %d" % (case+1, swaps)
	else:	
		print >> output, "Case #%d: IMPOSSIBLE" % (case+1)
