import sys
from collections import defaultdict
import operator

def do_line(line, case_num):
	nums = map(int, line.split(' '))
	total = sum(nums)

	xor = reduce(operator.xor, nums, 0)
	print nums
#	if xor != 0:
#		return "NO"

#	q = [[[] for x in range(total+1)] for y in range(len(nums))]
#	for i in range(total+1):
#		if nums[1] == i:
#			q[1][i] = [nums[1]]
#	for i in range(2, len(nums)):

#	q = defaultdict(list)
#	q[nums[0]] = [nums[0]]
#	for i in nums[1:]:
#		for k in q.keys():
#			q[k ^ n].append(q[k] + [i])

	#q = [[[] for x in range(1000000)] for y in range(len(nums))]
	q = [defaultdict(list) for y in range(len(nums))]
	
	#for i in range(total+1):
	#	if nums[0] == i:
	
	q[0][nums[0]].append([nums[0]])
	#for i, n in enumerate(nums[1:]):
	for i in range(1, len(nums)):
		n = nums[i]
		#for j in range(0,1000000):
		for j in q[i-1].keys():
			if q[i-1][j]:
				for x in q[i-1][j]:
					q[i][j].append(x)
				#q[i][j].append(q[i-1][j])
				#q[i][j] = q[i-1][j]
			for x in q[i-1][j]:
				q[i][j^n].append(x + [n])
		"""	if q[i-1][j^n]:
				#print q[i-1][j^n]
				for x in q[i-1][j^n]:
					q[i][j].append(x + [n])
				#q[i][j].append(q[i-1][j^n] + [n])
#				q[i][j] = q[i-1][j^n] + [n]
		"""
		q[i][n].append([n])
		#q[i][j] = [n]


	#print nums, xor, q[len(nums)-1][0]
#	for i,row in enumerate(q):
#		for j,col in row.iteritems():
#			if len(col) > 0:
#				print i,j, col
	m_sum = -1
	m = []
	num_sorted = sorted(nums)
	for xorsum, s in q[len(nums)-1].iteritems():
#		if len(s) > 0:
#			print xorsum, s
		for i, mine in enumerate(s):
			for j, his in enumerate(s):
				if i != j and sorted(his + mine) == num_sorted:
					my_sum = sum(mine)
#					print "Found two sets:", mine, his, "with xorsum of", xorsum, "my_sum:", my_sum,
					if my_sum > m_sum:
#						print "new best"
						m_sum = my_sum
						m = mine
					else:
						pass
						#print ''
	if m_sum == -1:
		return "NO"

	return m_sum

	

		



in_, out_f= sys.argv[1], sys.argv[1]+".out"
out = open(out_f, 'w')
with open(in_, 'r') as file:
	file.next()
	file.next()
	num = 1
	for line in file:
		ret = do_line(line, num)
		out.write("Case #%d: %s\n" % (num, ret))
		num += 1
		file.next()
