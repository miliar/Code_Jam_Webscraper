#!/usr/bin/python
import sys
import itertools
import math

def findsubsets(S,m):
    return itertools.combinations(S, m)

def best_result(score, is_surprising):
	if (not is_surprising):
		best = int(math.ceil(score / 3.0))
	else:
		best = 0
		for i in xrange(0,11):
			for j in xrange(0,11):
				for k in xrange(0,11):
					if (i + j + k != score):
						continue
					
					v1 = abs(i - j)
					v2 = abs(i - k)
					v3 = abs(j - k)
					if (max(v1,v2,v3) ==2):
						best = max(i,j,k)
	return best		

def calculate_posibility(P, SCORES, surprising):
	googlers = 0
	for i in xrange(len(SCORES)):
		score = SCORES[i]
		is_surprising= (i in surprising)
		result = best_result(score, is_surprising)
		if (result >= P):
			googlers += 1
	return googlers

def calculate(S, P, SCORES):
	subsets = findsubsets(range(len(SCORES)), S)
	
	result = 0
	for surprising in subsets:
		googlers = calculate_posibility(P, SCORES, surprising)
		if (googlers > result):
			result = googlers
	return result
		
	

def main():
	T = int(sys.stdin.readline())
	
	for i in xrange(T):
		line = sys.stdin.readline().strip()
		parts = line.split(' ')
		N = int(parts[0])
		S = int(parts[1])
		P = int(parts[2])
		SCORES = []
		sc = parts[3:]
		for v in sc:
			SCORES.append(int(v))
			
		value = calculate(S, P, SCORES)
		
		print "Case #" + str(i+1) + ": " + str(value)
main()
#print best_result(29, 0)
