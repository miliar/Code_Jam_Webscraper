#!/usr/bin/env python

import sys, os.path, re
import itertools, operator
import pdb

def initConvertor():
	
	cipheredData = [ "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
				"de kr kd eoya kw aej tysr re ujdr lkgc jv"]
	decipheredData = [ "our language is impossible to understand", "there are twenty six factorial possibilities",
					"so it is okay if you want to just give up" ]
	
	convertor = dict({' ': ' '})
	
	for sentenceNB in range(len(cipheredData)):
		sentence = cipheredData[sentenceNB]
		sentenceDeciph = decipheredData[sentenceNB]
		for i in range(len(sentence)):			
			if(convertor.has_key(sentence[i])):
				if convertor[sentence[i]] != sentenceDeciph[i]:
					print "Convertor mismatch for char %s: %s found instead of %s" %(sentence[i], sentenceDeciph[i], convertor[i])
			else:
				convertor[sentence[i]] = sentenceDeciph[i]
				
	# Check that we cover all input letters 
	charSet = set(map(chr, range(ord('a'), ord('z')+1)))
	remainingSet = charSet - set(convertor.values())
	for char in charSet: 
		if not convertor.has_key(char):
			#print "%s to identify" % char
			# Take the first available one
			for targetChar in remainingSet:
				if targetChar != char: # input char always <> output char
					convertor[char] = targetChar
					remainingSet.remove(targetChar)
					break
	if len(convertor) != 27: # a-z + space
		raise Exception("Incomplete convertor!")
	
	return convertor

def computeResult(convertor, line):

	result = ''.join([convertor[x] for x in line])
	return result


if __name__ == '__main__':

	if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
		inputFile = sys.stdin
	else:
		inputFile = open(sys.argv[1], 'r')

	testNB = 0

	#inputFormat = re.compile("^(.*)$")

	convertor = initConvertor()
	
	for line in inputFile:

		# Skip first line
		if testNB == 0:
			testNB += 1
			continue


		result = computeResult(convertor, line.lower().strip())
		print("Case #%s: %s" % (testNB, result))
		testNB+=1

exit(0)