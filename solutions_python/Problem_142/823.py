TEST = 0;#If 1 prints to console instead of file

import sys
class casesIO:
	def __init__(self,testfilepath,resultfilepath):
		self.testfile = open(testfilepath, 'r');
		self.outfile = open(resultfilepath, 'w');
		self.outlines = 0;
		nextline = self.testfile.readline();
		if not nextline:
			self.total = 0
		else:
			self.total = int(nextline);

	def readDelimiter(self):
		return int(self.testfile.readline());

	def readFormatedLine(self,formater):
		nextline = self.testfile.readline();
		return map(formater, nextline.split())
	def readLine(self):
		return self.testfile.readline().rstrip();
	def writeresult(self,case,result):
		if TEST:
			sys.stdout.write("Case #{0}: {1}\n".format(case,result));
		else:
			if self.outlines:
				self.outfile.write("\nCase #{0}: {1}".format(case,result));
			else:
				self.outfile.write("Case #{0}: {1}".format(case,result));
		self.outlines+= 1;

	def __del__(self):
		self.outfile.close()
		self.testfile.close()

io = casesIO("./A-small-attempt1.in","./resultA.txt");
def breakdown(word):
	breakdown = []
	prev = ''
	num = 0
	for c in word:
		if c != prev:
			if num > 0:
				breakdown.append(num)
			num = 1
			prev = c;
		else:
			num+=1

	breakdown.append(num)
	return breakdown;
def getMinimum(words,length):
	breakdowns = []
	for word in words:
		br = breakdown(word)
		breakdowns.append(br)
	min = 0
	for i in range(0,length):
		lmin = 99999;
		for cBreakdown in breakdowns:
			num = 0;
			for bdown in breakdowns:
				num += abs(cBreakdown[i] - bdown[i])
			if(num < lmin):
				lmin = num
			if(lmin == 0):
				break;
		min+= lmin		
	return min;

for i in range(1,io.total+1):
	Nwords = io.readDelimiter();
	characters = [];
	words = []
	prevC = ''
	word = io.readLine()
	for c in word:
		if prevC != c:
			characters.append(c);
			prevC = c
	words.append(word)
	prevC = ''
	check = True
	for j in range(1,Nwords):
		word = io.readLine()
		index = 0
		for c in word:
			if(c != prevC):
				if(index >= len(characters)):
					check = False
					break;
				if(characters[index] != c):
					check = False
					break;
				else:
					index+=1
					prevC = c
		if(index != len(characters)):
			check = False
			break;
		words.append(word)
	if(check):		
		io.writeresult(i,getMinimum(words,len(characters)))
	else:
		io.writeresult(i,'Fegla Won')
	

	 
	