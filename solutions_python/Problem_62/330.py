import sys

filename = sys.argv[1]

fd = open(filename, 'r')
op = open('output.dat', 'w')

def pro_func(count, lines):
	print count
	intersect = 0
	for line in lines:
		for o_line in lines:
			if o_line != line:
				print line, o_line
				if int(line[0]) < int(o_line[0]) and int(line[1]) > int(o_line[1]):					
					intersect += 1
	op.write('Case #' + str(count) + ': ' + str(intersect))
	op.write('\n')


for l1 in fd:	
	testcases = int(l1)
	flag = 1
	count = 0
	for l2 in fd:		
		data = l2.split()
		if flag == 1:
			n = int(data[0])
			to_read = n
			lines = []
			count += 1
			flag = 2
		elif flag == 2:
			lines.append(data)
			to_read -= 1
			if to_read == 0:
				pro_func(count, lines)
				flag = 1

