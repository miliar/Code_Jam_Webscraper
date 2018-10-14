#code jam 1b
import math;

input_file_name = "B-large.in";
output_file_name = "cj1b_out.txt";

#n - size of tSet
#s - number of upsets
#p - threshhold
#t - total scores
#return - max possible that meet p
#expected 	- ceil(tot/3)
#upset 		- (ceil(tot+1)/3)+1
def calc(n, s, p, tSet):
	set = [];
	expect = 0;
	upset = 0;
	for i in range(tSet.__len__()):
		expectedNum = int(math.ceil(float(tSet[i])/3.0));
		if (expectedNum >= p):
			expect+=1;
		if (tSet[i]>1):
			upsetNum = math.trunc((float(tSet[i]+1.0)/3.0))+1;
			if (upsetNum >= p):
				upset+=1;
		else:
			if (expectedNum >= p):
				upset+=1;
				
	if expect+s < upset:
		return expect + s;
	return upset;

input = [];

infile = open(input_file_name,"r");
while infile:
	line = infile.readline();
	if line:
		input.append(line.strip());
	else:
		break;

numcases = int(input[0]);

solutionText = [];
for i in range(numcases):
	j= i+1;
	inputArray = input[j].split(' ');
	formattedInput = [];
	for i in inputArray:
		formattedInput.append(int(i));
	argN = formattedInput.pop(0);
	argS = formattedInput.pop(0);
	argP = formattedInput.pop(0);
	output = "Case #"+str(j)+": "+str(calc(argN, argS, argP, formattedInput));
	print output;
	solutionText.append(output);
	

OUTFILE = open(output_file_name, "w");
OUTFILE.write("\n".join(solutionText));
OUTFILE.close();


