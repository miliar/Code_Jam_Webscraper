import sys
import math
import codecs


def seperate(x):
	items = []
	place = 0
	while place < len(x):
		if x[place] != '(' and x[place] != ')':
			items.append(x[place])
			place = place + 1
		else:
			ends = x.index(')',place+1)
			items.append(x[place+1:ends])
			place = ends+1
	return items

def check(x):
	count = 0
	
	for word in words:
		if charCorr(word,x):
			count=count+1
	return count
		
def charCorr(c, test):
	for b in range(0,length):
		if c[b] not in test[b]:
			return False
	return True
	
			

inputFile =  open('/Users/Anu/Projects/Python/b.txt', "r")
outputFile = open('/Users/Anu/Projects/Python/Alien_Big.txt', 'w')

input = inputFile.readline().split();
length = int(input[0])
numWords = int(input[1])
numTests = int(input[2])

words = []
cases = []

for i in range(0,numWords):
	words.append(inputFile.readline().strip())
	
for i in range(0,numTests):
	cases.append(inputFile.readline().strip())
	
#print 'Words:' , words
#print 'Test cases:' , cases
#for z in cases:
#	print seperate(z)

for i in range(0,numTests):
	print "Case #%d: %d" %(i+1 , check(seperate(cases[i])))
	outputFile.write("Case #%d: %d\n" %(i+1 , check(seperate(cases[i]))))

inputFile.close()
outputFile.close()

print '\n----------------Done!------------------\n'