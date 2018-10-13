# coding: shift-jis

def Order(s):
	l = list(s)
	l.sort()
	return reduce(lambda a,b: a+b, l)
	
	
import sys

f = file(sys.argv[1])

line_cnt = int(f.readline())


for number, s in enumerate(f):
	line = s.split()
	
	cntC  = int(line[0])
	
	combine = {}
	for rule in line[1:cntC+1]:
		combine[Order(rule[:2])] = rule[2]
	
	read = cntC+1
	cntD  = int(line[read])
	#ruleD = line[read+1:read+1+cntD]
	oppose = set()
	for rule in line[read+1:read+1+cntD]:
		oppose.add(Order(rule))
		
	
	read = read+1+cntD
	cntN = int(line[read])
	spell = line[read+1]
	
	# print number+1
	# print '\t', cntC, ruleC
	# print '\t', cntD, ruleD
	# print '\t', cntN, elements
	
	
	pos = 1
	while 1:
		if pos >= len(spell) or len(spell) < 2:
			break

		if pos == 0:
			pos = 1
			
		pair = Order(spell[pos-1:pos+1])
		
		if pair in combine:
			spell = spell[:pos-1] + combine[pair] + spell[pos+1:]
			#pos -= 1
			continue
		
			
		for pos2 in range(pos-1, -1, -1):
			pair = Order(spell[pos] + spell[pos2])
			if pair in oppose:
				spell = spell[pos+1:]
				pos = 0
				#spell = spell[:pos2] + spell[pos+1:]
				#pos = pos2 - 1
				break
			
		pos += 1
		
	if spell:
		ret = '[' + spell[0]
		for c in spell[1:]:
			ret += ', ' + c
		ret += ']'
	else:
		ret = '[]'
	print 'Case #%d:'%(number+1), ret
			
		
	
	#print 'Case #%d:'%(number+1), time
