'''
Created on 14 Apr 2013

@author: david
'''

def whatboard(currboard, i):
	retval = "Case #"+str(i)+": "
	for line in currboard:
		if (line.count("X") == 4):
			retval += "X won\n"
			return retval
		#print line.count("X"), line.count("T"), (line.count("X") == 3 and line.count("T") == 1)
		#exit(0)
		if (line.count("X") == 3 and line.count("T") == 1):
			retval += "X won\n"
			return retval
		if (line.count("O") == 4):
			retval += "O won\n"
			return retval
		if (line.count("O") == 3 and line.count("T") == 1):
			retval += "O won\n"
			return retval
	currflip = zip(*currboard)
	for line in currflip:
		print "lll ",line
		if (line.count("X") == 4):
			retval += "X won\n"
			return retval
		if (line.count("X") == 3 and line.count("T") == 1):
			retval += "X won\n"
			return retval
		if (line.count("O") == 4):
			retval += "O won\n"
			return retval
		if (line.count("O") == 3 and line.count("T") == 1):
			retval += "O won\n"
			return retval
	line=currboard[0][0]+currboard[1][1]+currboard[2][2]+currboard[3][3]
	if (line.count("X") == 4):
		retval += "X won\n"
		return retval
	if (line.count("X") == 3 and line.count("T") == 1):
		retval += "X won\n"
		return retval
	if (line.count("O") == 4):
		retval += "O won\n"
		return retval
	if (line.count("O") == 3 and line.count("T") == 1):
		retval += "O won\n"
		return retval

	line=currboard[0][3]+currboard[1][2]+currboard[2][1]+currboard[3][0]
	if (line.count("X") == 4):
		retval += "X won\n"
		return retval
	if (line.count("X") == 3 and line.count("T") == 1):
		retval += "X won\n"
		return retval
	if (line.count("O") == 4):
		retval += "O won\n"
		#print retval, "1"
		return retval
	if (line.count("T") == 1 and line.count("O") == 3):
		#print line,line.count("O"),line.count("T")
		retval += "O won\n"
		#print retval, "2333"
		#exit(0)
		return retval

	for line in currboard:
		if line.count(".")>0:
			retval += "Game has not completed\n"
			return retval
	retval += "Draw\n"
	#exit(0)
	return retval

def goo1():
	ctr = 1
	output=""
	lines = [line.strip() for line in open('A-large.in')]
	itera = int(lines[0])
	for i in range(1, itera+1):
		currboard = lines[ctr:ctr+4]
		output+=whatboard(currboard, i)
		#print "curr", currboard
		
		#print i
		
		
		ctr+=5
	print output
	f = open('large.txt','w')
	f.write(output) # python will convert \n to os.linesep
	f.close()

import math
def is_square(integer):
	root = math.sqrt(integer)
	if int(root + 0.5) ** 2 == integer: 
		return True
	else:
		return False
	
def is_pal(word):
    return word == word[::-1]

def getnum(s1, s2):
	ctr = 0
	for i in range(s1,s2+1):
		if (is_square(i) and is_pal(str(i)) and is_pal(str(int(math.sqrt(float(i)))))):
			ctr+=1
	return ctr

def goo2():
	output=""
	lines = [line.strip() for line in open('C-small-attempt0.in')]
	lines = lines[1:]
	iii = 1
	print lines
	for line in lines:
		sp = line.split(" ")
		ctr = getnum(int(sp[0]), int(sp[1]))
		output+="Case #"+str(iii)+": "+str(ctr)+"\n"
		iii+=1
	print output
	f = open('small.txt','w')
	f.write(output) # python will convert \n to os.linesep
	f.close()

if __name__ == '__main__':
	goo2()