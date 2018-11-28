import sys
def howManyFriends(counts):
	n = len(counts)
	numPeopleStanding = 0
	friendsNeeded = 0
	for shyness, numPeople in enumerate(counts):
		while numPeopleStanding < shyness:
			friendsNeeded+=1
			numPeopleStanding+=1
		numPeopleStanding += numPeople
	return friendsNeeded

def main():
	lines = [x.strip() for x in sys.stdin.readlines()]
	n = int(lines[0])
	for i, line in enumerate(lines[1:]):
		cts = [int(ch) for ch in line.split()[1]]
		friends = howManyFriends(cts)
		print "Case #{0}: {1}".format(i+1, friends)

if __name__ == '__main__':
	main()