#!/usr/bin/env python

import sys

f = open(sys.argv[1])
cases = f.readlines()
len_cases = int(cases[0])
for i in range(1, len_cases*10, 10):
	rep1 = cases[i][:-1]
	rep2 = cases[i+5][:-1]
	cards1 = cases[i+1][:-1].split() + cases[i+2][:-1].split() + cases[i+3][:-1].split() + cases[i+4][:-1].split()
	cards2 = cases[i+6][:-1].split() + cases[i+7][:-1].split() + cases[i+8][:-1].split() + cases[i+9][:-1].split()
	result = []
	for card in cards1[int(rep1)*4-4:int(rep1)*4]:
		if card in [cards2[int(rep2)*4-4], cards2[int(rep2)*4-3], cards2[int(rep2)*4-2], cards2[int(rep2)*4-1]]:
			result.append(card)
	if result != []:
		if len(result) > 1:
			print "Case #%d: Bad magician!" % int((i+9)/10)
		else:
			print "Case #%d: %s" % ((i+9)/10, result[0])
	else:
		print "Case #%d: Volunteer cheated!" % int((i+9)/10)
f.close()