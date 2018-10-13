import math
#import copy
from datetime import datetime

#import psyco
#psyco.full()

def printMsg(msg):
	if (True):
		print msg
		
##############################################

class Solver:
	_dict = []
	_wordlen = 0
	_tree = {}

	def __init__(self, w):
		self._wordlen = w
		None

	def reset(self):
		None

	def answer(self, tw):
		ans = "0"
		cnt = 0
		c = []
		open = False
		tmp = []
		#print tw
		for i in range(0, len(tw)):
			x = tw[i]
			if open:
				if x == ")":
					c += [tmp, ]
					tmp = []
					open = False
				else:
					tmp += [x, ]
			else:
				if x == "(":
					open = True
				else:
					c += [[x], ]
		
		#print c
		for w in self._dict:
			i = 0
			ok = True
			while i < self._wordlen and ok:
				ok = w[i] in c[i]
				i += 1
			
			if ok:
				cnt += 1
					
		print tw, cnt
		ans = cnt
		return ans

	def readDict(self, inf, dictSize):
		for i in range(0, dictSize):
			word = inf.readline().strip()
			self._dict += [word, ] 
		#print self._dict 
		#self.buildTree()
	
	def buildTree(self):
		for w in self._dict:
			cur = self._tree
			for i in range(0, self._wordlen):
				c = w[i]
				if cur.has_key(c):
					cur = cur[c]
				else:
					cur[c] = {}
					cur = cur[c]
		print self._tree
			
##############################################

prjId = "qr_a"

_MIN_CASES = 999
testCase = "large"
#testCase = "small"

#infilename="./data/A-"+testCase+"-practice.in"
#infilename="./data/A-small-attempt0.in"
#infilename="./data/large_sample.in"
infilename="./data/A-large.in"
outfile = "./out/"+prjId+"_"+ testCase +"_ans.out"

inf = open(infilename, "r")
outf = open(outfile, "w")

headerline = inf.readline()
(wordlen, dictSize, numCases) = headerline.split()

print numCases, dictSize, wordlen

numCases = int(numCases)

solver = Solver(int(wordlen))
stTime = datetime.now()
solver.readDict(inf, int(dictSize))
#print solver._dict

print "Start", stTime
for i in range(1, min(numCases+1, _MIN_CASES +1)):
    line = inf.readline().strip()
    solver.reset()
    ans = solver.answer(line)
    print "Case #%d:" % i, ans
    outf.write("Case #%d: %s" % (i, ans))
    outf.write("\n")
    #break

endTime = datetime.now()
print "End",  endTime
print endTime - stTime

inf.close()
outf.close()
