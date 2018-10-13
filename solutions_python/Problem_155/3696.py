from decimal import *

def writeToFile( caseNum, answer ):
   outputStr = 'Case #' + str(caseNum) + ': ' + str(round(answer,7)) + '\n';
   print(outputStr);
   print("----");
   f2.write(outputStr);

f1 = open('D:\Documents\GoogleCodeJam\StandingOvation-small-attempt1.in', 'r');
f2 = open('D:\Documents\GoogleCodeJam\StandingOvation-small-attempt1.out', 'w');

linenum = 0;
numtests = 0;

for line in f1:
	print(line);
	if linenum > 0:
		vals = line.split(' ');
		max = int(vals[0]);
		counts = (vals[1]);
		
		currStanding = int(counts[0]);
		currFriends = 0;
		
		i = 1;
		while i <= max:
			testStr = "Shyness = ";
			testStr += str(i);
			testStr += ", Friends = ";
			testStr += str(currFriends);
			testStr += ", Standing = ";
			testStr += str(currStanding);
			testStr += ", To Gain = ";
			testStr += counts[i];
			print(testStr);
			
			if currStanding < i and int(counts[i]) > 0:
				currFriends += (i - currStanding);
				currStanding += currFriends;
				
			currStanding += int(counts[i]);
				
			i+=1;
		
		
		writeToFile(linenum, currFriends);
		
	linenum += 1;

f1.close()
f2.close();

