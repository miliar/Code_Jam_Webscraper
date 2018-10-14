#!/usr/bin/python
cases = int(raw_input())

results = []

for i in xrange(cases):
	max_shiness, levels = raw_input().split()
	
	invites = 0
	audience = 0
	
	index = 0
	for s in levels:
		add = 0
		if index > audience and int(s) > 0:
			add = index - audience
			
		invites += add
		
		audience += int(s) + add
		index += 1
		
	results.append(invites)
	
index = 1
for case in results:
	print "Case #%d: %d" % (index, case)
	index +=1