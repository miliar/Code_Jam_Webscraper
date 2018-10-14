#!/usr/bin/python

import sys


samples = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

outputs = ["our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"]

lut = []

for i in range(0,26):
	lut.append('-')

lut[ord('y') - 97] = 'a'
lut[ord('q') - 97] = 'z'
lut[ord('e') - 97] = 'o'
lut[ord('z') - 97] = 'q'


for i in range(0, len(samples)):
	for j in range(0, len(samples[i])):
		if samples[i][j] != ' ':
			if (lut[ord(samples[i][j]) - 97] != '-') and (lut[ord(samples[i][j]) - 97] != outputs[i][j]):
				print "we have a problem %d %d %s %s" %(i, j, lut[ord(samples[i][j]) - 97], outputs[i][j])
				print "%s (%d) -> %s (%d)" %(samples[i][j], ord(samples[i][j]) - 97, outputs[i][j], ord(outputs[i][j]) - 97)
			else:
				lut[ord(samples[i][j]) - ord('a')] = outputs[i][j]

#inputs = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

count = int(sys.stdin.readline())

for i in range(0, count):
	input = sys.stdin.readline()
	result = ""
	for j in range(0, len(input)):
		if ord(input[j]) < 32:
			break
		elif input[j] == ' ':
			result += ' '
		else:
			result += (lut[ord(input[j]) - 97])
	print "Case #%d: %s" %(i + 1, result)

