import operator

def analyse(n,r,o,y,g,b,v):

	letters = "ROYGBV"
	valids = [(2,3,4),(3,4,5),(4,5,0),(5,0,1),(0,1,2),(1,2,3),(0,1,2,3,4,5)]
	origN = n
	origNumbers = [r,o,y,g,b,v]
	numbers = [r,o,y,g,b,v]
	
	#print("")
	#print(numbers)
	if y + g + b < r or g + b + v < o or b + v + r < y or v + r + o < g or r + o + y < b or o + y + g < v:
		return "IMPOSSIBLE"

	
	answers = []
	lastI = 6
	while n > 0:

		if n == 2:
			f, s = [i for i in range(6) if numbers[i] > 0]

			if f in valids[answers[0]] and s in valids[answers[-1]]:
				answers += [s,f]
			else:
				answers += [f,s]
			n = 0

		else:

			bestI = float('inf')
			bestScore = 0
			bestSides = 2

			scores = [None if k not in valids[lastI] else (numbers[k], (1 if numbers[(k+1)%6] > 0 else 0) + (1 if numbers[(k-1)%6] > 0 else 0)) for k in range(6)]

			for k in range(6):
				if scores[k]:
					score, sides = scores[k]
					if score > bestScore or (score == bestScore and sides >= bestSides):
						bestScore = score
						bestSides = sides
						bestI = k

			lastI = bestI
			answers.append(lastI)

			#print(scores)
			#print(answers)
			numbers[lastI] -= 1
			n -= 1

		#print(answers)

	answer = ""
	valid = True
	for i in range(origN):
		answer += letters[answers[i]]

		if (answers[i] not in valids[answers[(i+1)%origN]]) or (answers[i] not in valids[answers[(i-1)%origN]]):
			valid = False
			print("ERROR illegal seq", answers[(i-1)%origN], answers[i], answers[(i+1)%origN])

	for i in range(6):
		if origNumbers[i] != answers.count(i):
			valid = False
			print("ERROR illegal count ", i, letters[i])

	if not valid:
		print("ERROR!", answer, answers)

	print(answer)
	return answer

def next(values):
	return max(enumerate(values), key=operator.itemgetter(1))


def run(name):
	lines = [l for l in open(name + ".in", mode='r')]
	m = int(lines[0])
	
	out = open(name + ".out",mode='w')
	for i, line in enumerate(lines[1:]):
		n,r,o,y,g,b,v = [int(s) for s in line.rstrip().split(" ")]
		answer = analyse(n,r,o,y,g,b,v)
		out.write("Case #" + str(i+1) + ": " + answer + "\n")
	out.close()

run("B-small-attempt0")