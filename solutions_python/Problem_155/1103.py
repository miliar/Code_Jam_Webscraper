t = int(input())

for x in range(1, t+1):
	line = input().split()
	people = list(map(int, line[1]))
	invites = 0
	standing = 0
	
	for y in range(0, int(line[0]) + 1):
		if standing + invites >= y:
			standing += people[y]
		else:
			invites += y - (standing + invites)
			standing += people[y]
	print ('Case #{0}: {1}'.format(x, invites))