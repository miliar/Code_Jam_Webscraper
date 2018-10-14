# Solution to "Magic Trick" for Google Code Jam 2014
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
import string

def inputData():
	with open(sys.argv[1], 'r') as f:
		numCases = int(f.readline())
		for c in range(numCases):
			data = []
			for guess in range(2):
				row = int(f.readline())
				cards = [f.readline().split() for _ in range(4)]
				data.append((row, cards))
			yield data


f = open(sys.argv[2], 'w')

for c,case in enumerate(inputData()):
	rows = [data[1][data[0]-1] for data in case]
	matches = [x for x in rows[0] if x in rows[1]]
	if len(matches) == 1:
		answer = matches[0]
	elif len(matches) == 0:
		answer = "Volunteer cheated!"
	else:
		answer = "Bad magician!"
	f.write("Case #%d: %s\n"%(c+1, answer))

f.close()