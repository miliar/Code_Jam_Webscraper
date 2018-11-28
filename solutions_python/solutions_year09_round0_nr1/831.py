#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
from sys import argv

def mkpattern(string):
	i,poss = 0,[]
	while i<len(string):
		if string[i] != '(': poss.append([string[i]])
		else:
			j=i=i+1
			while string[i] != ')': i+=1
			poss.append(list(string[j:i]))
		i+=1
	return poss

def wordsInPattern(pattern,words):
	return sum(all( (x in y) for x,y in zip(w,mkpattern(pattern)) ) for w in words)

class BadFileError(Exception):
	def __init__(self,msg):
		self.msg = msg
	def __str__(self):
		return repr(self.msg)

def mygetline(f):
	s = f.readline()
	if s=="": raise BadFileError("File '" + argv[1] + "' was incorrectly formatted.")
	else: return s.strip()

if len(argv) < 2:
	raise BadFileError("Not enough arguments!")
	quit()

f = open(argv[1])

l,d,n = tuple(int(s) for s in mygetline(f).split())

words = []
for x in xrange(d): words.append(mygetline(f))

patterns = []
for x in xrange(n): patterns.append(mygetline(f))

if f.readline() != "" or len(words) != d or len(patterns) != n:
	raise BadFileError("File '" + argv[1] + "' was incorrectly formatted.")
else:
	f.close()
	i=1
	for p in patterns:
		print "Case #" + str(i) + ": " + str(wordsInPattern(p,words))
		i+=1
