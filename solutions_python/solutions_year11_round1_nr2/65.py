#!/usr/bin/env python

import operator
import math
from pprint import pprint

log = False
def getCount(chosen_word, L, words):
	if log:
		print ''
		print '###'
		
		print 'chosen_word: ', chosen_word
	
	match = str(chosen_word)

	same_len_words = set([w for w in words if len(w) == len(chosen_word)])

	chars_in_words = [c for c in L if any(c in w for w in same_len_words)]
	if log:
		print 'chars_in_words: ', chars_in_words
	
	same_len_words.remove(chosen_word)
	if log:
		print 'same_len_words: ', same_len_words
	
	points = 0
	for e in chars_in_words:
		if not any(e in w for w in (same_len_words | set([chosen_word]))):
			continue
		if log:
			print 'guess ', e
		
		same_len_words = set([y.replace(e, '.') for y in same_len_words])
		if e in chosen_word:
			match = match.replace(e, '.')
				
			if log:
				print 'match ', match
		else:
			points += 1
			
		killset = set()
		for w in same_len_words:
			for z, x in zip(w, match):
				if x == '.' or z == '.':
					if z != x:
						killset.add(w)
						continue
		same_len_words -= killset
		if log:
			print 'killset ', killset,len(same_len_words)
			print 'same_len_words ', same_len_words
		
		if len(same_len_words) == 0:
			break
			
		if match == '.' * len(match):
			break
			
	if log:
		print points, match

	return points
	
assert getCount('banana', 'abcdefghijklmnopqrstuvwxyz', ['banana','caravan','pajamas']) == 0
assert getCount('caravan', 'abcdefghijklmnopqrstuvwxyz', ['banana','caravan','pajamas']) == 0
assert getCount('pajamas', 'abcdefghijklmnopqrstuvwxyz', ['banana','caravan','pajamas']) == 1

assert getCount('banana', 'etaoisnhrdlcumwfgypbvkjxqz', ['banana','caravan','pajamas']) == 0
assert getCount('caravan', 'etaoisnhrdlcumwfgypbvkjxqz', ['banana','caravan','pajamas']) == 1
assert getCount('pajamas', 'etaoisnhrdlcumwfgypbvkjxqz', ['banana','caravan','pajamas']) == 0

assert getCount('potato', 'zyxwvutsrqponmlkjihgfedcba', ['potato','tomato','garlic','pepper']) == 0
assert getCount('tomato', 'zyxwvutsrqponmlkjihgfedcba', ['potato','tomato','garlic','pepper']) == 0
assert getCount('garlic', 'zyxwvutsrqponmlkjihgfedcba', ['potato','tomato','garlic','pepper']) == 1
assert getCount('pepper', 'zyxwvutsrqponmlkjihgfedcba', ['potato','tomato','garlic','pepper']) == 1

						
if __name__=='__main__':    
	with open('B-small-0.in') as f:
		lines = f.readlines()

	problems = []

	line_num = 1
	while line_num < len(lines):
		N, M = map(int, lines[line_num].split())
		line_num += 1

		words = []
		for i in range(N):
			words.append(lines[line_num].strip())
			line_num += 1

		s = []
		for i in range(M):
			s.append((words, lines[line_num].strip()))
			line_num += 1
		problems.append(s)

	#~ pprint(problems)

	for line_num, s in enumerate(problems):
		the_words = []
		
		for problem in s:
			words, L = problem
			if log:
				print L, len(L)
			
			max_points = -1
			max_point_word = ''
			
			for chosen_word in words:
				points = getCount(chosen_word, L, words)
				
				if max_points < points:
					
					max_points = points
					#~ print max_points, chosen_word
					max_point_word = chosen_word
			the_words.append(max_point_word)

		print 'Case #%s: %s' % (line_num+1, " ".join(the_words))#>>output_file, 




