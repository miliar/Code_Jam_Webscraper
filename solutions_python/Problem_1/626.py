#Andre Bluehs
#hello@andrebluehs.net

newFile = open("A-small-attempt3.in");
totalCases = 0;

# these will end up being 2d arrays
# containing the case number, and 
# associated engines, queries, or switches
# for that case number.
engines = []; 
queries = [];
switches = [];


counter = 0;
totalEngines = 99999; #needs to start way out of range
totalQueries = 99999; #needs to start way out of range
casesCounter = 0;
output = "";

# this for loop populates the engines and queries arrays
for line in newFile:
	if (counter == 0):
		totalCases = int(line);
		# this for loop creates the 2d arrays
		# with the format [caseNumber] [] starting at 0
		for i in range(totalCases):
			engines.append(i);
			engines[i] = [];
			queries.append(i);
			queries[i] = [];
			switches.append(i);
			queries[i] = [];
		counter = 1;
	if (totalCases > 0):
		if (counter == 2):
			totalEngines = counter + int(line);
		if (counter in range(3, totalEngines+1)):
			engines[casesCounter].append(line);
		if (counter == (totalEngines+1)):
			totalQueries = counter  + int(line);
		if (counter in range(totalEngines+2, totalQueries+1)):
			queries[casesCounter].append(line);
		if (counter == totalQueries+1):
			totalCases-=1;
			counter=2;
			casesCounter+=1;
			totalEngines = 2+int(line);
	counter+=1;

zeroCounter = 0;
#this for loop checks the easy case of 0 switches
for count in range(len(engines)):
	for thing in engines[count]:
		if thing in queries[count]:
			zeroCounter += 1;
	if zeroCounter < len(engines[count]):
		switches[count] = -1;
		zeroCounter = 0;
	else:
		switches[count] = 0;
		zeroCounter = 0;

# this for loop counts all the remaining switches.
# it does so by populating an array with the queries in order.
# it does not put in duplicate entries.
# once all engines have been put into the array, 
# it is time to switch engines, as all possible choices prior 
# to the last engine have been used.


for count in range(len(queries)):
	newCounter = 0;
	usedArray = [];
	for thing in queries[count]:
		newCounter +=1;
		if thing not in usedArray:
			usedArray.append(thing);
			if len(usedArray) == len(engines[count]):
				switches[count] +=1;
				usedArray = [];
				usedArray.append(thing);
		if newCounter == len(queries[count]):
				usedArray = [];

		
for count in range(len(switches)):
	if switches[count] == -1:
			total = 0;
	else:
			total = int(switches[count]);
	output += "Case #" + str(count+1) + ": " + str(total) + "\n";
	
print output;



		

		

		