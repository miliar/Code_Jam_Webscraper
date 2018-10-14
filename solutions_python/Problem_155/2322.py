from sys import stdin

cases = int(stdin.readline())

for i in range(0, cases):
	line = stdin.readline()
	maxS = int(line.split()[0])
	people = line.split()[1]
	nStanding = int(people[0])
	invites = 0
	for j in range(1, len(people)):
		while (nStanding<j):
			invites += 1
			nStanding += 1 
		nStanding += int(people[j])
	print "Case #" + str(i+1) + ": " + str(invites)