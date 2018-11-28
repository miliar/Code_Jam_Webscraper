def main():
	fin = open('B-small-attempt3.in','r')
	fout = open('output.txt','w')
	
	T = int(fin.readline())
	
	for i in range(T):
		
		N,M = [int(x) for x in fin.readline().strip().split(' ')]
		
		words = []
		lists = []
		for j in range(N):
			words.append(fin.readline().strip())
		for j in range(M):
			lists.append(fin.readline().strip())
		
		bestWords = []
		for j in range(M):
			bestWord = ''
			bestScore = 0
			for k in range(N):
				#run sim for this word
				ln = len(words[k])
				progress = [False] * ln
				curWords = [x for x in words if len(x) == ln]
				curScore = 0
				alreadyTried = []
				
				for c in lists[j]:
					alreadyTried.append(c)
					if len(curWords) == 1:
						break
					if checkC(curWords,c):
						upScore = True
						for p in range(ln):
							if words[k][p] == c:
								progress[p] = c
								upScore = False
						if upScore:
							curScore += 1
					curWords = [x for x in curWords if validate(x,progress,ln,alreadyTried)]
				if curScore > bestScore:
					bestScore = curScore
					bestWord = words[k]
			
			if bestWord	== '':
				bestWords.append(words[0])
			else:	
				bestWords.append(bestWord)
		
		print 'Case #' + str(i+1) + ': ' + ' '.join(bestWords)
		fout.write('Case #' + str(i+1) + ': ' + ' '.join(bestWords) + '\n')

def checkC(curWords,c):
	for word in curWords:
		if c in word:
			return True
	return False
	
def validate(word,progress,ln,charlist):
	for i in range(ln):
		if ((progress[i] and progress[i] != word[i]) or (not progress[i] and (word[i] in charlist))):
			return False
	return True
if __name__ == '__main__':
	main()
