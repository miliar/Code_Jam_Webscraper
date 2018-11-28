#!/usr/bin/env
from sys import stdin
import string

output = open('output2.txt', 'w')
case_no = 1

for line in stdin.readlines()[1:]:
	line = line.strip().split(' ')
	N = int(line[0]) # number of googlers
	S = int(line[1]) # number of suprising
	p = int(line[2]) # target score
	scores = line[3:]
	triplets = []
	
	if p == 0:
		result = N
		# print 'Case #'+str(case_no)+': '+str(result)+'\n'
		output.write('Case #'+str(case_no)+': '+str(result)+'\n')
		case_no += 1
		continue
	
	# calculate maximum non-suprising scores (base-scores)
	for i in range(len(scores)):
		t = int(scores[i])
		triplet = [t//3, t//3, t//3]
		for j in range(t%3):
			triplet[j] += 1  
		triplets.append(triplet)

	result = 0
	# print 'S =', S
	for item in triplets:
		if item[0] >= p: result +=1
		elif S==0: continue
		elif item[0]+1 == p and item[0]==item[1] and item[1]!=0:		
			item[0] += 1
			item[1] -= 1
			item.append('*')
			S -= 1
			result +=1
		
		# print 'P =',str(p),'-',item
	# print 'Case #'+str(case_no)+': '+str(result)+'\n'
	output.write('Case #'+str(case_no)+': '+str(result)+'\n')
	case_no += 1
			
output.close()

