import time
import sys
import string
starttime,sol = time.time(), 0

BASE = "abcdefghijklmnopqrstuvwxyz "
GOOGLERESE = "ynficwlbkuomxsevzpdrjgthaq "

def englishToGooglerese(n, encrypted = ""):
	for x in n:
		encrypted += GOOGLERESE[BASE.index(x)]
	return encrypted

def googlereseToEnglish(n, plain = ""):
	for x in n:
		plain += BASE[GOOGLERESE.index(x)]
	return plain	
print


print	
file_1 = open('A-small-attempt0.in','r')
file_2 = open('GJ_1_sol.txt', 'w')

numoflines = int(file_1.readline())

for x in range(numoflines):
	print >> file_2, "Case #{0}: {1}".format(x+1, googlereseToEnglish(file_1.readline().strip()).strip())
print






print "================================================================"	
print "Answer ", sol, "found in", time.time() - starttime
print "================================================================"	