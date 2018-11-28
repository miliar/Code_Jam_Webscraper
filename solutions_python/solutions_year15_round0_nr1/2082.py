import fileinput

def solveTc(tcLine):
	spacePos = tcLine.find(' ');
	maxShyness = int(tcLine[0:spacePos]);
	audience = tcLine[spacePos+1:].strip();

	#print('\tMax shyness: %i; Audience: %s' % (maxShyness, audience));

	friendsToBeAdded = 0;
	currentShyness = 0;
	peopleStanding = 0;
	for i in audience:
		if (int(i) > 0 and (currentShyness > peopleStanding)):
			needMoreFriends = currentShyness - peopleStanding;
			friendsToBeAdded += needMoreFriends;
			peopleStanding += needMoreFriends;

		peopleStanding += int(i);
		currentShyness += 1;

	return friendsToBeAdded;

cases = -1;
index = -1;

for line in fileinput.input():
	if (cases == -1):
		cases = int(line);
		index = 1;
	elif (index != -1):
		result = solveTc(line);
		print('Case #%i: %i' % (index, result));
		index += 1;

