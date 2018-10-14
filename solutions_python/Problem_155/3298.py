a_input = open('A-large.in','r')
t = int(a_input.readline())
audience = []
for i in range(t):
	line = a_input.readline()
	line = line.split()
	audience.append([int(i) for i in line[1] ])
def standup(audience):
	peopleUp = 0
	peopleNeeded = 0
	for i in range(len(audience)):
		if i > peopleUp:
			peopleNeeded += (i - peopleUp)
			peopleUp += i - peopleUp
			peopleUp += audience[i]
		else:
			peopleUp += audience[i]
	return peopleNeeded

for i in range(len(audience)):
	print "Case #%d: %d" % (i+1,standup(audience[i]))


