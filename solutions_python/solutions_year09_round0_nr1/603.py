#! /usr/bin/python


def parseTest(test):
	result = []
	i = 0
	while i < len(test):
		if test[i] == '(':
			i+=1
			tmp = []
			while test[i]!=')':
				tmp += test[i]
				i += 1
			result += [tmp]
		else:
			result += test[i]	
		i += 1
	return result	

L, D, N = raw_input().split(' ')
L = int(L)
D = int(D)
N = int(N)
dict = []

for i in range(D):
	dict += [raw_input()]	
for i in range(N):
	count = 0
	teststring = raw_input()
	
	tests = parseTest(teststring)
	for word in dict:
		correct = True
		for j in range(len(word)):
			if word[j] not in tests[j]: correct = False
		if correct: count += 1
	print "Case #"+str(i+1) + ": " + str(count)			
