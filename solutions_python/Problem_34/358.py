import types

class TrieNode:
	def __init__(self):
		self.children = {}
	
	def add(self, string):
		if string == None or len(string) == 0:
			return
		ch = string[0]
		if ch in self.children:
			if len(string) > 1:
				if self.children[ch] == None:
					self.children[ch] = TrieNode()
					print "You input a word with different length or duplicate"
				self.children[ch].add(string[1:])
			else:
				print "You input duplicate words"
		else:
			if len(string) > 1:
				self.children[ch] = TrieNode()
				self.children[ch].add(string[1:])
			else:
				self.children[ch] = None
	
	def countMatches(self, letters):
		#print letters
		if letters == None or len(letters) == 0:
			return 0
		ch = letters[0]
		if len(letters) == 1:
			if type(ch) == types.StringType:
				if ch in self.children:
					return 1
				else:
					return 0
			else:	# set
				cnt = 0
				for c in ch:
					if c in self.children:
						cnt += 1
				return cnt
		else:
			if type(ch) == types.StringType:
				if ch in self.children:
					return self.children[ch].countMatches(letters[1:])
				else:
					return 0
			else:
				cnt = 0
				for c in ch:
					if c in self.children:
						cnt += self.children[c].countMatches(letters[1:])
				return cnt

class WordPattern:
	def __init__(self, string):
		self.letters = []
		if string != None and len(string) > 0:
			idx = 0
			groupStarted = False
			group = None
			for ch in string:
				if ch == '(':
					groupStarted = True
					group = set()
				elif ch == ')':
					groupStarted = False
					self.letters.append(group)
				elif groupStarted:
					group.add(ch)
				else:
					self.letters.append(ch)
			#print self.letters


class AlienDic:
	def __init__(self):
		self.root = TrieNode()
	
	def addWord(self, word):
		self.root.add(word)
	
	def countMatches(self, patternString):
		if patternString == None or len(patternString) == 0:
			return 0
		pattern = WordPattern(patternString)
		return self.root.countMatches(pattern.letters)


import sys

fileNameIn = sys.argv[1]
#print fileNameIn[-3:]
if fileNameIn[-3:] != ".in":
	sys.exit()
fileNameOut = fileNameIn[0:-3] + ".out"
#print fileNameOut

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()


idx = 0
line = lines[idx].split(' ')	# new line?
wordlen = int(line[0])
wordcnt = int(line[1])
testcnt = int(line[2])
#print "wordlen = {0}, wordcnt = {1}, testcnt = {2}".format(wordlen, wordcnt, testcnt)
idx += 1

aliendic = AlienDic()

for i in range(wordcnt):
	aliendic.addWord(lines[idx][0:-1])
	idx += 1

fileOut = open(fileNameOut, 'w')

for i in range(testcnt):
	line = lines[idx][0:-1]
	#print line
	idx += 1
	fileOut.write("Case #{0}: {1}\n".format(i+1, aliendic.countMatches(line)))

