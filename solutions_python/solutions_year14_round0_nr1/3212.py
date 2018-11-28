#!/usr/bin/env python3

def main():
	tests = int(input())
	for i in range(tests):
		firstRow = int(input())
		firstTable = []
		for _ in range(4):
			firstTable.append(input())
		firstChoices = set(firstTable[firstRow - 1].split()) # one-indexing!
		secondRow = int(input())
		secondTable = []
		for _ in range(4):
			secondTable.append(input())
		secondChoices = set(secondTable[secondRow - 1].split())
		results = firstChoices.intersection(secondChoices)
		verdict = len(results)
		if verdict == 0:
			print("Case #%d: Volunteer cheated!" % (i+1))
		elif verdict == 1:
			print("Case #%d: %s" % (i+1, list(results)[0]))
		else:
			print("Case #%d: Bad magician!" % (i+1))

if __name__ == '__main__':
	main()
