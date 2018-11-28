#!/usr/bin/python
import sys


if len(sys.argv) == 3:
	lines = open(sys.argv[1], 'r').readlines()
	fw = open(sys.argv[2], 'w')
else:
	sys.exit('Usage: %s in_filename out_filename' % sys.argv[0])


"""
lines = ['3'
,'4 O 2 B 1 B 2 O 4'
,'3 O 5 O 8 B 100'
,'2 B 2 B 1']
"""

numofcases = int(lines[0])
cursor = 1
for i in range(0, numofcases):
	
	param = lines[cursor].replace('\n','').split(' ')
	cursor += 1
	
	numoforders = int(param[0])
	
	orders = []
	
	for j in range(0, numoforders):
		orders.append({'hall':param[1+j*2], 'id':int(param[1+j*2+1])})
		
	print orders
	
	ra_pos = 1
	rb_pos = 1
	last_col = orders[0]['hall']
	total = 0
	for j in range(0, numoforders):
		if orders[j]['hall']=='O':
			duration = abs(ra_pos - orders[j]['id']) + 1 #move and push
			ra_pos = orders[j]['id']
			total += duration 
			next_pos=0
			for k in range(j, numoforders):
				if orders[k]['hall']=='B':
					next_pos = orders[k]['id']
					break
			if next_pos>0:
				l = next_pos - rb_pos
				if abs(l)>0:
					if abs(l)>duration:
						rb_pos += l/abs(l)*duration
					else:
						rb_pos += l
		else:
			duration = abs(rb_pos - orders[j]['id']) + 1 #move and push
			rb_pos = orders[j]['id']
			total += duration 
			next_pos=0
			for k in range(j, numoforders):
				if orders[k]['hall']=='O':
					next_pos = orders[k]['id']
					break
			if next_pos>0:
				l = next_pos - ra_pos
				if abs(l)>0:
					if abs(l)>duration:
						ra_pos += l/abs(l)*duration
					else:
						ra_pos += l
		print ra_pos, rb_pos, total, orders[j]
	result = total
		
	print 'Case #' + str(i+1) + ': ' + str(result)
	fw.write('Case #' + str(i+1) + ': ' + str(result) + '\n')

fw.close()

