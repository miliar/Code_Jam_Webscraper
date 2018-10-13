import sys

f = open(sys.argv[1])
T = int(f.readline())

def readList(size):
	l = list()
	for _ in range(size):
		l.append(list(f.readline()))
	return l

def getChar(word, index):
	if index < len(word):
		return word[index]
	else:
		return None

def run():
	count = 0
	i = 0
	while True:
		wordLength = max(map(len, words))
		if i >= wordLength:
			break
		
		char = words[0][i]
		if len(filter(lambda w: w[i] == char, words)) != len(words):
			return 'Fegla Won'
		
		nextChars = map(lambda w: getChar(w, i+1), words)
		sameCount = 0
		otherCount = 0
		for n in nextChars:
			if n == char:
				sameCount += 1
			else:
				otherCount += 1
		
		if otherCount > sameCount:
			for word in words:
				if getChar(word, i+1) == char:
					del word[i+1]
					count += 1
		else:
			for word in words:
				if getChar(word, i+1) != char:
					word.insert(i, char)
					count += 1
		
		i += 1
	
	return count

for t in range(T):
	N = int(f.readline())
	words = readList(N)
	
	result = run()
	print 'Case #%d:' % (t + 1), result
