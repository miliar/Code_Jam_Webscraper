#!/usr/bin/env python
import math
import sys
import os
from os import system
import collections

def identical(strings):
	prev_ordered = ""
	for str in strings:
		olist = []
		ordered = ""
		#print ",", str
		#print "*", ordered, prev_ordered
		for s in list(str):
			if len(olist) != 0 and s == olist[-1]:
				continue
			else:
				olist.append(s)
		ordered = "".join(olist)
		#print ordered
		#print "p", prev_ordered
		if prev_ordered != "" and ordered != prev_ordered: return -1
		prev_ordered = ordered
	
	#print prev_ordered

	#counters = []
	#for str in strings:
	#	counters.append(collections.Counter(str))
	#print prev_ordered
	freqs_r = []
	for str in strings:
		freq = []
		count = 0
		i = 0
		for s in str:
			if i < len(prev_ordered) and s == prev_ordered[i]:
				count += 1
			else :
				freq.append(count)
				i += 1
				count = 1
		freq.append(count)
		freqs_r.append(freq)
	freqs = [sorted(list(x)) for x in zip(*freqs_r)]	
	#print freqs
	# prev_ordered is the basic string.
	#freqs = [sorted([count[c] for count in counters ]) for c in prev_ordered]
	#print freqs
	total = 0
	for freq in freqs:
		mid = int(len(freq)/2)
		num = freq[mid]
		#print "num", num
		for f in freq:
			total += abs(f-num)
	return total

		
fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
string = fp.readline()
T = int(string)
for t in range(T):
	N = int(fp.readline())
	strings = []
	for i in range(N):
		row = fp.readline().strip()
		strings.append(row)

	num = identical(strings)
	if num == -1:
		ret = "Fegla Won"
	else:
		ret = str(num)

	fout.write('Case #%d: %s\n'%((t+1),ret))
