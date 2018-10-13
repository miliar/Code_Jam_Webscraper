# gcj stock functions

def readItems():
	line = raw_input();
	line = line.strip();
	line = line.split(" ");
	items = [];
	for item in line:
		try:
			if (item.find(".") >= 0):
				finalItem = float(item);
			else:
				finalItem = int(item);
		except ValueError:
			finalItem = item; # not an int or a float, must be a string.
		items.append(finalItem);
	return items;

def readString():
	line = raw_input();
	line = line.strip();
	return line;

items = readItems();
testCases = items[0];

for i in range(0,testCases):
	testCase = readItems();
	
	numGooglers = testCase[0];
	surprising = testCase[1];
	atLeast = testCase[2];
	scores = testCase[3:];
	
	scores.sort(); # sort them lowest to highest.
	belowMinimum = 0; # Googlers that CANNOT meet the desired min best.
	for score in scores:
		avg = score / 3;
		rem = score % 3;
		if (avg >= atLeast):
			# we can meet this greatest value as the average with no remainder overflow.
			# hence it works and will always work from this point out.
			break;
		elif (avg == atLeast-1 and rem > 0):
			# we are one below the average needed to clear the best, with remainder factored it.
			# hence it works and will always work from this point out.
			break;
		elif (avg == atLeast-1 and avg > 0 and rem == 0 and surprising > 0):
			# we can make this a "surprising" result... but it comes at a cost.
			# since rem = 0, we subtract 1 from the worst and add one to the best
			# to get it to the desired min best score.
			surprising -= 1;
		elif (avg == atLeast-2 and rem == 2 and surprising > 0):
			# we can make this a "surprising" result... but it comes at a cost.
			# since we have 2 left over from the average, add them to one result to bump it
			# up to the desired best.
			surprising -= 1;
		else:
			# NO way to make this a desired result.
			belowMinimum += 1;
	result = numGooglers - belowMinimum;
	print "Case #"+str(i+1)+": "+str(result);
