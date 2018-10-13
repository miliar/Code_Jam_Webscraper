#!/usr/bin/env python
# encoding: utf-8

case_count = int(raw_input())

for n in xrange(case_count):
	
	num = raw_input()
	if len(num) == 1:
		print 'Case #%d: %s0' % (n + 1, num)
		continue
		
	num_list = [int(x) for x in list(num)]
	
	changed = False
	for i in xrange(-2, 0-len(num_list)-1, -1):
		l1 = num_list[i+1:]
		l2 = filter(lambda x:x>num_list[i], l1)
		if len(l2) > 0:
			num_to_changed = min(l2)
			l1.remove(num_to_changed)
			l1.append(num_list[i])
			l1.sort()
			print 'Case #%d: %s' % (n + 1, num[:i] + str(num_to_changed) + ''.join([str(x) for x in l1]))
			changed = True
			break;
			
	if not changed:
		first = min(filter(lambda x:x>0, num_list))
		num_list.remove(first)
		num_list.append(0)
		num_list.sort()
		print 'Case #%d: %s' % (n + 1, str(first) + ''.join([str(x) for x in num_list]))
			
		

