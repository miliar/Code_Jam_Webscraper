#!/usr/bin/env python
# encoding: utf-8
"""
welcometocodejam.py

Created by Jack on 2009-09-03.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os, re

ALPHAS = 'welcomtdja '

REGEX = re.compile('[^w]*(w.*e.*l.*c.*o.*m.*e.* .*t.*o.* .*c.*o.*d.*e.* .*j.*a.*m)[^m]*')
REGEX2 = re.compile('[^' + ALPHAS + ']')

TEXT_ARRAY = ['w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm']

def count_match(alphas_pos, text_pos=-1, last_alpha_pos=-1):
	
	total = 0
	if text_pos == 17:
		return len(filter(lambda x: x > last_alpha_pos, alphas_pos[TEXT_ARRAY[text_pos+1]]))
	
	#print text_pos
	#print last_alpha_pos
	#print filter(lambda x: x > last_alpha_pos, alphas_pos[TEXT_ARRAY[text_pos+1]])
	for next_alpha_pos in filter(lambda x: x > last_alpha_pos, alphas_pos[TEXT_ARRAY[text_pos+1]]):
		total += count_match(alphas_pos, text_pos+1, next_alpha_pos)
	
	return total

def main():
	
	n = int(raw_input())
	
	texts = []
	for i in range(n):
		texts.append(raw_input())
	
	case_no = 1
		
	for text in texts:
		if len(text) < 19:
			print 'Case #%d: 0000' % case_no
		else:
			m = REGEX.match(text)
			if not m:
				print 'Case #%d: 0000' % case_no
			else:
				orgin_text = REGEX2.sub('', m.groups()[0])
				#print orgin_text
				alphas_pos = {}
				for i in range(len(orgin_text)):
					if not alphas_pos.has_key(orgin_text[i]):
						alphas_pos.update({orgin_text[i]: [i]})
					else:
						alphas_pos[orgin_text[i]].append(i)
				
				count = str(count_match(alphas_pos))
				
				if len(count) < 4:
					count = ''.join(['0' for i in range(4-len(count))]) + count
				else:
					count = count[-4:]
					
				print 'Case #%d: %s' % (case_no, count)
				
					
		case_no += 1
					
if __name__ == '__main__':
	main()

