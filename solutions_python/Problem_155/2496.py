# Author: Dakota Leonard
# Problem: Standing Ovation

numCases = input();
case = [];
caseNumber = 0;

#Get all input
for i in range(0,int(numCases)):
	case.append(raw_input());

#Process all input
for c in case:
	#Split the input
	sMax, audience = c.split();
	currentlyClapping = 0;
	addedMembers = 0;
	for n in range(0,int(sMax)+1):
		#If not eneough people are clapping, add enough till others will clap
		if currentlyClapping < n:
			addedMembers += n-currentlyClapping;
			currentlyClapping += n-currentlyClapping;
		currentlyClapping += int(audience[n]);
	caseNumber += 1
	print("Case #" + str(caseNumber) + ": " + str(addedMembers));
