
from __future__ import print_function
import fileinput


lineNumber = 0;
maxLineNumber = 0;
for line in fileinput.input():
	if lineNumber ==0:
		maxLineNumber = float(line);
	else:
		splitInput = line.split(' ');
		totalStanding = 0;
		totalInvited = 0;
		currentShyness = 0;
		maxNum = int(float(splitInput[0]));
		for s in splitInput[1]:
			if currentShyness <= maxNum:
				
				num = int(float(s));	
				if num > 0 and totalStanding < currentShyness:
					totalInvited += currentShyness - totalStanding;
					totalStanding +=totalInvited;
				totalStanding +=num;
				currentShyness += 1;
		print("Case #", lineNumber, ": ", totalInvited, sep=''); 
	lineNumber +=1;
