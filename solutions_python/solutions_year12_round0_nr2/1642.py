import sys

f = open('B-large.in', 'r')
out = open('output.txt', 'w')
testCases = int(f.readline())
count = 0

while (count < testCases):
	input = f.readline()
	input = input.split()
	constestants = input[0]
	surprises = int(input[1])
	
	min_score = int(input[2])*3 - 2
	if min_score < 0:
		min_score = 1
	if int(input[2]) == 0:
		min_score = 0
		
	min_surprising = int(input[2])*3 - 4
	if min_surprising < 0:
		min_surprising = 1
	if int(input[2]) == 0:
		min_surprising = 0
		
	scores = input[3:]
	result = 0
	for score in scores:
		if int(score) >= min_score:
			result += 1
		else:
			if int(score) >= min_surprising and surprises > 0:
				result += 1
				surprises -= 1
	output = 'Case #' + (str)(count+1) + ": " + (str)(result) + '\n'
	out.write(output)
	count += 1

f.close()
out.close()