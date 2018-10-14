import math
from itertools import groupby

def parseString(string):
	frequencies = []
	letters = []
	groups = ["".join(grp) for num, grp in groupby(string)]
	for group in groups:
		letters.append(group[0])
		frequencies.append(len(group))
	return letters, frequencies



def trial():
	N = int(raw_input())
	letterFrequencies = []
	totalFrequencies = []
	sampleLetters, frequencies = parseString(raw_input())
	letterFrequencies.append(frequencies)
	for frequency in letterFrequencies[0]:
		totalFrequencies.append(float(frequency))
	for n in range(1, N):
		letters, frequencies = parseString(raw_input())
		if letters != sampleLetters:
			return "Fegla Won"
		else:
			letterFrequencies.append(frequencies)
			for i in range(len(letters)):
				totalFrequencies[i] += frequencies[i]

	moves = 0
	for i in range(len(letters)):
		mean = round(totalFrequencies[i]/N)
		for letterFrequency in letterFrequencies:
			moves += abs(mean - letterFrequency[i])
	return int(moves)

T = int(raw_input())
for t in range(1,T+1):
	print "Case #%d:" % t,
	print trial()
