#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(inp):
	HAPPY = "+"
	SAD = "-"
	length = len(inp)
	S = inp[:inp.index(' ')]
	pattern = list(S)
	K = int(inp[len(pattern)+1:])
	count = 0
	try:
		sad_index = pattern.index(SAD)
	except ValueError: 
		return count
	ended = False
	while not ended:
		if (len(pattern) - sad_index) < K:
				return 'IMPOSSIBLE'
		for i in range(K):
			if pattern[sad_index + i] == HAPPY:
				pattern[sad_index + i] = SAD
			elif pattern[sad_index + i] == SAD:
				pattern[sad_index + i] = HAPPY
		count += 1
		try:
			sad_index = pattern.index(SAD)
		except ValueError:
			ended = True
		
	return count
				
		
	return "pattern " + pattern + " S " + S

if __name__ == '__main__':
	testcases = int(input())

	for case in range(testcases):
		inp = input()
		print("Case #{}: {}".format(case+1, main(inp))) 
