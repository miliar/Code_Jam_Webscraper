#!/usr/bin/env python
# encoding: utf-8
"""
alien_language.py

Created by Jack on 2009-09-03.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys, os, re

def parse_pattern(pattern):
	
	ret = ''
	
	need_line = False
	for i in range(len(pattern)):
		if pattern[i] == '(':
			need_line = True
			ret += pattern[i]
			continue
		elif pattern[i] == ')':
			need_line = False
			ret += pattern[i]
			continue
			
		ret += pattern[i]
		if need_line and pattern[i+1] != ')':
			ret += '|'
			
	return ret

def main():
	
	l, d, n = raw_input().split(' ')
	
	words = []
	for i in range(int(d)):
		words.append(raw_input())
		
	patterns = []
	for i in range(int(n)):
		p = raw_input()
		patterns.append(parse_pattern(p))
		#print parse_pattern(p)

	case_no = 1
	for pattern in patterns:
		match_count = 0
		reg = re.compile('^' + pattern + '$')
		for word in words:
			if reg.match(word):
				match_count += 1
		print 'Case #%d: %d' % (case_no, match_count)
		case_no += 1
		
if __name__ == '__main__':
	main()

