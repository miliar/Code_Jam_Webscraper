import string

f = open('B-large.in', 'r')
g = open('output.txt', 'w')

n = int(f.readline())
count = 1

while count <= n:
	line = f.readline()
	if '\n' in line:
		line = line[:-1]
		
	line = line.split()
	N = int(line[0])
	S = int(line[1])
	p = int(line[2])
	scores = line[3:]
	for i in range(len(scores)):
		scores[i] = int(scores[i])
		
	maxScoreCount = 0
	for score in scores:
		if score % 3 == 1 and ((score + 2) / 3) >= p:
			maxScoreCount += 1
		elif score % 3 == 2:
			if ((score + 1) / 3) >= p:
				maxScoreCount += 1
			elif S > 0 and ((score + 1) / 3) == (p - 1):
				S -= 1
				maxScoreCount += 1
		else:
			if (score / 3) >= p:
				maxScoreCount += 1
			elif S > 0 and ((score + 3) / 3) == p and score >= 3:
				S -= 1
				maxScoreCount += 1
		
	g.write("Case #" + str(count) + ": " + str(maxScoreCount) + '\n')

	count += 1
	
f.close()
g.close()