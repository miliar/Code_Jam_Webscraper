# -*- coding: utf-8 -*-
INPUT  = ["A-small.in","A-large.in"]
OUTPUT = ["alien_small.out","alien_large.out"]
DEBUG  = 0 
RUN    = 1


def read(run):
	dict = []

	line = input.readline()[:-1].split(" ")
	var_L = int(line[0])
	var_D = int(line[1])
	var_N = int(line[2])

	if DEBUG>0:
		print var_L,var_D,var_N

	for i in xrange(var_D):
		dict.append(input.readline()[:-1])
	dict.sort()
	return var_L,var_D,var_N,dict

def getWord(line):
	word = []
	open = False
	letters = ""
	for i in line:
		if i=="(":
			open = True
			continue
		elif i==")":
			open = False
			word.append(letters)
			letters=""
			continue
		elif open:
			letters+=i
		else:
			word.append(i)
	return word

def getPossibilities(word,dict,var_L):
	possible = dict[:]
	for group in xrange(var_L):
		words = 0
		while words < len(possible):
			if DEBUG > 5:
				print "Words:",possible[words]
				print "letter:",word[group]
				print "toFind:",possible[words][group]
				print "Possible:",possible
			if word[group].find(possible[words][group])==-1:
				possible.remove(possible[words])
			else:
				words+=1
			if DEBUG > 2:
				print "Words:",words
				print "possible:",len(possible)
				print "\n"
	if DEBUG>0:
		print "Possible:",possible,"\n\n"
	return len(possible)

def outputPossibilities(output,i,var_K):
	output.write("Case #"+str(i+1)+": "+str(var_K)+"\n")
	output.flush()

input = open(INPUT[RUN],"r")
output = open(OUTPUT[RUN],"w")

var_L,var_D,var_N,dict = read(RUN)



for i in xrange(var_N):
	line = input.readline()[:-1]
	word = getWord(line)
	outputPossibilities(output,i,getPossibilities(word,dict,var_L))
print dict
