t = int(raw_input())
for i in xrange(1,t+1):
	n, k = [int(x) for x in raw_input().strip().split(" ")]
	free = {n:1}
	# print free
	for j in range(k):
		m = max(free.keys())
		# print m
		right = m/2
		if m % 2 == 0:	#creating splits
			# print "even"
			left = right - 1
			if right in free.keys():
				free[right] += 1
			else:
				free[right] = 1
			if (left) in free.keys():
				free[left] += 1
			else:
				free[left] = 1
		else:
			# print "odd"
			left = right
			if right in free.keys():
				free[right] += 2
			else:
				free[right] = 2
		# print "Left: {}; Right: {}".format(left,right)
		free[m] -= 1
		if free[m] == 0:	#decreasing old max by one
			del free[m]
		# print free
	print "Case #{}: {} {}".format(i, right, left)




# t = int(raw_input())
# for i in xrange(1,t+1):
# 	n, k = [int(x) for x in raw_input().strip().split(" ")]
# 	n = [n]
# 		# print n
# 	for j in range(k-1): #does this process for all users except last one
# 		m = n.index(max(n))
# 		if n[m] % 2 == 0:
# 			n[m] /= 2
# 			n.insert(m, (n[m]-1))
# 		else:
# 			n[m] /= 2
# 			n.insert(m, n[m])
# 		# print n
# 	m = n.index(max(n))	#last one's computation done here
# 	if n[m] % 2 == 0:
# 		z = n[m]/2
# 		y = z - 1
# 	else:
# 		z = n[m]/2
# 		y = z
# 	print "Case #{}: {} {}".format(i, z, y)