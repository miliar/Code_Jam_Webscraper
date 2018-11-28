def canstand(shy,peopleUp):
	return (peopleUp >= shy)

def solve(smax,s):
	peopleUp = 0
	friends = 0
	for x in range(smax+1):
		if int(s[x]) > 0:
			if(not canstand(x,peopleUp)):
				friends += (x - peopleUp)
				peopleUp += (x - peopleUp)
			peopleUp += int(s[x])	
	return str(friends)
t = input()
inputs = []
for x in range(t):
	line = raw_input()
	line = line.split()
	smax = int(line[0])
	inputs.append((smax,line[1]))

for a in range(t):	
	print "Case #"+str(a+1)+": "+solve(inputs[a][0],inputs[a][1])