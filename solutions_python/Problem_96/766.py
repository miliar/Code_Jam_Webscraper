import math

def canSurprice(s):
	if s >= 2:
		return True;
	return False;
sourceFile = "small.in";
outputFile = "small.out";

s_handler = open(sourceFile, 'r');
o_handler = open(outputFile, 'w');

T = s_handler.readline();

for i in range(1, int(T)+1):
	line = s_handler.readline().strip();
	splits = line.split(" ");
	N = int(splits[0]);#total number
	S = int(splits[1]);#surprising number
	p = int(splits[2]);#best score
	total = [];
	result = 0;
	for j in range(0, N):
		total.append(int(splits[j+3]));
	total = sorted(total);
	for k in range(0, len(total)):
		score = total[k];
		while (score > 3*p):
			score -= 3;
		if canSurprice(total[k]) == True and abs(score-3*p)<=4:
			result += 1;
		else:
			if p == 0:
				result += 1;
			else:
				if total[k] == 1:
					result += 1;	
		
	for k in range(len(total) - result, len(total)):
		score = total[k];
		while (score > 3*p):
			score -= 3;
		if (abs(score-3*p) > 2):
			S -= 1;
	if (S < 0):
		result += S;
		
	print result;	
				

	o_handler.write("Case #" + str(i) + ": " + str(result) + "\n");

s_handler.close();
o_handler.close();
