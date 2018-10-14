#!/usr/bin/python
import math as m


def xwin(s):
	if(len(s) != 4):
		print 'Bad input!'
		return
	if((s.count("X") == 3 and s.count("T") == 1) or  (s.count("X") == 4)):
		return 1
	else:
		return 0


def owin(s):
	if(len(s) != 4):
		print 'Bad input!'
		return
	if((s.count("O") == 3 and s.count("T") == 1) or  (s.count("O") == 4)):
		return 1
	else:
		return 0


# r = ["","","",""]
# c = ["","","",""]
# d = ["",""]

def whowon(r):

	answer = ""

	c = []
	for i in range(0,4):
		c.append("")
		for j in range(0,4):
			c[i] = c[i] + r[j][i]

	d = []
	d.append("")
	d.append("")
	for i in range(0,4):
		d[0] = d[0] + r[i][i]
		d[1] = d[1] + r[i][3-i]

	for fix in c:
		if(xwin(fix)):
			if(answer == ""):
				answer = "X won"

		if(owin(fix)):
			if(answer == ""):
				answer = "O won"

	for fix in r:
		if(xwin(fix)):
			if(answer == ""):
				answer = "X won"

		if(owin(fix)):
			if(answer == ""):
				answer = "O won"

	for fix in d:
		if(xwin(fix)):
			if(answer == ""):
				answer = "X won"

		if(owin(fix)):
			if(answer == ""):
				answer = "O won"


	if(answer == ""):
		for fix in r:
			if(fix.count(".") > 0):
				answer = "Game has not completed"

	if(answer == ""):
		answer = "Draw"
	
	return answer

f = open('input.txt');
o = open('output.txt','w')

i = 0
for lines in f:


	if(i == 0):
		i = i + 1 
		r = []
		continue

	if(i%5 == 0):
		i = i + 1
		print "Case #" + str(int(m.floor(i/5))) + ": " + "\n" 
		print r 
		print "\n" + str(whowon(r)) + "\n"
		o.write("Case #" + str(int(m.floor(i/5))) + ": " + str(whowon(r)) + "\n") 
		r = []
		continue

	r.append(lines[0:4])
	i = i + 1
	print


#The Last Case.
print "Case #" + str(int(m.floor(i/5))) + ": " + "\n" 
print r 
print "\n" + str(whowon(r)) + "\n"
o.write("Case #" + str(int(m.floor(i/5))) + ": " + str(whowon(r)) + "\n") 