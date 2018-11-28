from sys import argv

f = open(argv[1])
o = open(argv[1].replace('.in', '.out'), 'w')

test_count = int(f.readline())

for case_number in range(1, test_count+1):
#for case_number in range(1, 5):
	index, audience = map(str.rstrip, f.readline().split(' '))

	audience = map(int, audience)
	index = int(index)
	#print audience
	num_standing = 0
	num_friends = 0
	
	for idx, mem in enumerate(audience):
		num_new_friends = 0
		if mem == 0:
			continue
		elif(num_standing < idx):
			num_new_friends = idx - num_standing
			num_standing += num_new_friends
			num_friends += num_new_friends
		num_standing += mem
		#print mem, num_standing, num_new_friends, num_friends

	#output = max(0, last - sum(audience))
	#print audience
	print 'Case #%d: %d' % (case_number, num_friends)
	o.write('Case #%d: %d\n' % (case_number, num_friends))