import sys

filename = sys.argv[1]

fd = open(filename, 'r')
op = open('output.dat', 'w')

def pro_func(dir_present, dir_to_create, count):		
	#print dir_present
	#print dir_to_create
	pre_sub = []
	for p_path in dir_present:
		#print p_path		
		dir_split = p_path.split("/")
		sub_paths = []
		for i in range(1, len(dir_split) + 1):
			sub_paths.append('/'.join(dir_split[:i]))
		pre_sub.extend(sub_paths[1:])
	
	to_make = 0
	for path in dir_to_create:
		#print path
		dir_split = path.split("/")		
		sub_paths = []
		for i in range(1, len(dir_split) + 1):
			sub_paths.append('/'.join(dir_split[:i]))
		sub_paths = sub_paths[1:]
		#print sub_paths
		if path in dir_present:
			continue
		else:
			for i in range(len(sub_paths)):
				if sub_paths[i] not in pre_sub:
					to_make += len(sub_paths) - i
					pre_sub.extend(sub_paths)
	op.write('Case #' + str(count) + ': ' + str(to_make))
	op.write('\n')

for l1 in fd:
	years = []
	testcases = int(l1)
	flag = 1
	count = 0
	dir_present = []
	dir_to_create = []
	for l2 in fd:		
		data = l2.split()
		if flag == 1:			
			count += 1
			n = int(data[0])
			m = int(data[1])
			if n > 0:			
				flag = 2
			elif m > 0:
				flag = 3
		elif flag == 2:			
			n -= 1
			dir_present.append(l2.split()[0])
			if n == 0:
				flag = 3
		elif flag == 3:
			m -= 1
			dir_to_create.append(l2.split()[0])
			if m == 0:
				pro_func(dir_present, dir_to_create, count)
				dir_present = []
				dir_to_create = []
				flag = 1
				
