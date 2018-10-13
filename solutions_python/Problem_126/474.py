#!/usr/bin/python2
# AUTHOR:   rj
# FILE:     /media/files/projects/contests/google-code-jam-2013/round-1-c/consonants/small.py
# CREATED:  17:26:42 12/05/2013
# MODIFIED: 17:46:10 12/05/2013

import sys
def vowels(c):
	return c=='a' or c=='o' or c =='i' or c=='u' or c=='e';
def brute_force(s,n): 
	l = len(s); 
	count = 0; 
	for i in range(l): 
		mc = 0; 
		for j in range(i,l): 
			if (not vowels(s[j])): 
				mc += 1; 
			else: 
				mc = 0; 
			if (mc>=n):
				count+=l-j;
				break
	return count
def run(case):
	s,n = map(str,sys.stdin.readline().split()); 
	n = int(n); 
	print 'Case #'+str(case)+': '+str(brute_force(s,n)) 

N = int(raw_input()); 
for i in range(1,N+1): 
	run(i);
