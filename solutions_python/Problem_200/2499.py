import re
from collections import OrderedDict

lineNumb = 0;

def isTidy(number):
	chFirst = ""
	for ch in number:
		if (chFirst == ""):
			chFirst = ch
		elif (chFirst > ch):
			return False
		else:
			chFirst = ch
	return True

def findTidy(number):

	l = list(str(number))

	coso = "".join(l)
	while(not isTidy(coso)):
		chFirst = ""

		print "coso:" + coso
		for n in range(len(l)):
			print(n)
			if (chFirst == ""):
				chFirst = l[n]
			else:
				if int(chFirst) > int(l[n]):
					l[n-1] = int(l[n-1]) -1
					print "n: " +str(n)
					for tmp in range(n,len(l)):
						l[tmp] = 9
					print l
					chFirst = l[n]
				else:
					chFirst = l[n]
		coso = "".join(map(str,l))
		print "coso after:" + coso

	return "".join(map(str,l))



def evaluate (maxNum, iteration):

	tidy = 0
	out_file = open("B-large.out","a")

	if (len(maxNum) == 1):
		out_file.write("Case #" + str(iteration) + ": " + str(maxNum) + "\n")
		return

	maxNum = findTidy(maxNum)
	maxNum = int(maxNum)

	out_file.write("Case #" + str(iteration) + ": " + str(maxNum) + "\n")

	out_file.close()

with open("B-large.in") as file:
	iteration = 0
	for line in file:
		if(lineNumb == 0):
			lineNumb = line
		else:
			evaluate(line.strip('\n'), iteration)
		iteration = int(iteration) + 1