#!/usr/bin/env python
# encoding: utf-8
"""
Snapper.py

Created by Thomas Espitau for the GCJ 2010.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os



def snapper(N,K):
	if ( K % (2**N )) == ( 2**N - 1 ): return 'ON'
	else:						return 'OFF'



def solution(N,lines):
	tmp = ''
	for i in range(N):
		tmp += 'Case #%s: %s\n' % (str(i+1), snapper(int(lines[i][0]), int(lines[i][1])))
	return tmp
	
	
if __name__ == '__main__':
	N = int(raw_input())
	lines = [tuple(raw_input().split()) for i in xrange(N)]

	print solution(N,lines)