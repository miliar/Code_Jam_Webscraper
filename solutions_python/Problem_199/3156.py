#!/usr/bin/python3
import random

inputFile = "1_small.in"

def processTestCase(pancakes, flipperSize):
	def generateDatasets(amount, rightmost):
		for x in range(amount):
			yield set([random.randint(pancakes.index('-'), rightmost)])
	
	def addFlip(dset):
		possible = list(possibleFlips - dset)
		return dset | set([random.choice(possible)])

	def getFitnessList(sets):
		for dset in sets:
			yield (getFitness(dset), dset, flipPancakes(dset))

	def getFitness(dset):
		output = flipPancakes(dset)
		if '-' not in output:
			return 100000
		start = 1
		streak = 0
		lastStreak = 0
		otherStreak = 0
		fitness = 1000
		for pc in output:
			if pc == '+':
				if start:
					continue
				else:
					if streak > 0:
						if streak % flipperSize == 0:
							fitness += 100 * streak / flipperSize
						else:
							fitness -= 100 * streak % flipperSize
						if lastStreak + otherStreak == flipperSize:
							fitness += 10 * lastStreak
							fitness += 10 * (streak - lastStreak) / flipperSize
							fitness -= 10 * abs((streak - lastStreak) % flipperSize)
						lastStreak = streak
						streak = 0
						otherStreak = 0
					otherStreak += 1
			else:
				if start:
					start = 0
				streak += 1
		if streak > 0:
			if streak % flipperSize == 0:
				fitness += 10 * streak / flipperSize
			else:
				fitness -= 10 * streak % flipperSize
		return fitness

	def flipPancakes(dset):
		newPancakes = pancakes
		for flip in dset:
			newPancakes = newPancakes[0:flip] + newPancakes[flip:flip + flipperSize].replace('+', '.').replace('-', '+').replace('.', '-') + newPancakes[flip + flipperSize:]
		return newPancakes

	def breed(set1, set2):
		same = set1 & set2
		different1 = list(set1 - same)
		different2 = list(set2 - same)
		new1 = same | set(different1[:int(len(different1) / 2)]) | set(different2[int(len(different2) / 2):])
		new2 = same | set(different2[:int(len(different2) / 2)]) | set(different1[int(len(different1) / 2):])
		return (new1, new2)
	
	if not '-' in pancakes:
		return 0
	if pancakes.count('-') % 2 != 0 and flipperSize % 2 == 0:
		return -1
	if len(pancakes) - flipperSize < flipperSize:
		if '+' in pancakes[-flipperSize:flipperSize] and '-' in pancakes[-flipperSize:flipperSize]:
			return -1
	rightmost = len(pancakes) - flipperSize
	sets = generateDatasets(len(pancakes) * 16, rightmost)
	fitnesses = list(getFitnessList(sets))
	fitnesses.sort(key=lambda e: e[0], reverse=True)
	if fitnesses[0][0] == 100000:
		return len(fitnesses[0][1])
	possibleFlips = set(range(pancakes.index('-'), len(pancakes) - flipperSize))
	while 1:
		sets = []
		for f in fitnesses:
			try:
				sets.append(addFlip(f[1]))
			except:
				randList = []
				for x in f[1]:
					randList.append(random.choice(list(possibleFlips - set(randList))))
				sets.append(set(randList))
		fitnesses = list(getFitnessList(sets))
		fitnesses.sort(key=lambda e: e[0], reverse=True)
		if fitnesses[0][0] == 100000:
			return len(fitnesses[0][1])
		sets = []
		for i in range(0, len(fitnesses), 2):
			new1, new2 = breed(fitnesses[i][1], fitnesses[i + 1][1])
			sets.append(new1)
			sets.append(new2)
		fitnesses = list(getFitnessList(sets))
		fitnesses.sort(key=lambda e: e[0], reverse=True)
		if fitnesses[0][0] == 100000:
			return len(fitnesses[0][1])

with open(inputFile) as f:
	content = f.read().split("\n")[1:-1]
	i = 1
	for line in content:
		pancakes, flipperSize = line.split(" ")
		outputs = []
		for x in range(20):
			try:
				outputs.append(processTestCase(pancakes, int(flipperSize)))
			except Exception as e:
				pass
		if len(outputs) == 0:
			print("Case #%d: IMPOSSIBLE" % i)
			i += 1
			continue
		print("Case #%d: " % i, end="")
		print("IMPOSSIBLE" if min(outputs) < 0 else min(outputs))
		i += 1

