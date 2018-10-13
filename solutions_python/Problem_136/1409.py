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

io = casesIO("./B-large.in","./result2.txt");

for i in range(1,io.total+1):
	case = io.readFormatedLine(float);
	#Check input data
	if len(case) != 3:
		break; #bad input
	C = case[0];
	if C < 1 or C > 10000:
		break; #bad input
	F = case[1];
	if F < 1 or F > 100:
		break; #bad input
	X = case[2];	
	if X < 1 or X > 100000:
		break; #bad input

	elapsedtime = 0;
	speed = 2;
	totaltime = 0;
	while True:
		totaltime = elapsedtime + X / speed;
		nexttime = elapsedtime + C/speed + X/(speed + F);
		if nexttime > totaltime:
			break
		else:
			elapsedtime+= C/speed;
			speed+= F;

	io.writeresult(i,totaltime)
	