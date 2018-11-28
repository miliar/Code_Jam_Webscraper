f = open("A-large.in", 'r')
problems = []
numprobs = 0
for i,line in enumerate(f):
	line = line.split('\n')[0]
	if i < 1:
		numprobs = int(i)
	else:
		max_shy, prob = line.split(' ')
		max_shy, prob = int(max_shy), [int(x) for x in prob]
		problems.append((max_shy, prob))


def difs(prob):
	sums = []
	s = 0
	for i, e in enumerate(prob):
		sums.append(i-s)
		s = s+e
	return sums

def answer(p):
	return str(max(difs(p[1])))


sol = open("opera_large.txt", "w")
for i, p in enumerate(problems):
	if i > 0:
		sol.write("\n")
	sol.write("Case #"+str(i+1)+": "+answer(p))