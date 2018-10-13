#!/usr/bin/env python
# encoding: utf-8

case_count = int(raw_input())

for n in xrange(case_count):
	
	org = raw_input()
	
	num_list = list(set(list(org)))
	
	base = len(num_list)
	if base == 1:
		base = 2
	
	num_len = len(org)
	
	a2n = {org[0]: 1}
	now_num = 0
	
	for x in xrange(1, num_len):
		if not a2n.has_key(org[x]):
			a2n[org[x]] = now_num
			now_num += (2 if now_num == 0 else 1)
		
	result = 0	
	for x in xrange(num_len):
		result += a2n[org[x]] * pow(base, num_len - x - 1)
		
	print 'Case #%d: %d' % (n + 1, result)
	

