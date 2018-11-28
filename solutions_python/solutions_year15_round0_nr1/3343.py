f = open('A-large.in').read().splitlines()

output = []

for case in xrange(1, len(f)):
	y = 0
	max, audience = f[case].split()
	standing = 0
	for shyIndex in xrange(len(audience)):
		people = int(audience[shyIndex])
		if standing >= shyIndex:
			pass
		elif standing < shyIndex:
			additionalFriends = shyIndex - standing
			y += additionalFriends
			standing += additionalFriends
		standing += people
		
	output.append("Case #" + str(case) + ": " + str(y))


with open('output', 'w') as f:
	f.write("\n".join(output))