#!/usr/bin/env python
# encoding: utf-8

def perm(k, m):
	global prison_to_release
	
	if k == m - 1:
		count_bribe(prison_to_release)
	else:
		for i in xrange(k, m):
			tmp = prison_to_release[k]
			prison_to_release[k] = prison_to_release[i]
			prison_to_release[i] = tmp
			#print prison_to_release
			#print ''
			
			perm(k + 1, m)
			
			tmp = prison_to_release[k]
			prison_to_release[k] = prison_to_release[i]
			prison_to_release[i] = tmp
			#print prison_to_release
			#print ''

def count_bribe(release_order):
	global prison_count
	
	prisons = [1 for x in xrange(prison_count)]
	
	bribe = 0
	for i in release_order:
		prisons[i - 1] = 0
		
		#print i
		for x in xrange(i - 2, -1, -1):
			if prisons[x] == 0:
				break;
			bribe += 1
		#print bride
		
		for x in xrange(i, prison_count):
			if prisons[x] == 0:
				break;
			bribe += 1
		#print bride
		#print prisons
		#print ''
		
	global min_bribe
	if bribe < min_bribe:
		min_bribe = bribe
	

case_count = int(raw_input())

prison_to_release = []
prison_count = 0
min_bribe = 999999

for n in xrange(case_count):
	
	prison_count, release = raw_input().split()
	prison_count = int(prison_count)
	release = int(release)
	
	prison_to_release = [int(x) for x in raw_input().split(' ')]
	
	min_bribe = 999999
	
	perm(0, release)
	
	print 'Case #%d: %d' % (n + 1, min_bribe)
		
		
		
			
			
			
	

