T = int(raw_input())

for i in xrange(T):
	N = int(raw_input())
	inherit = []
	for j in xrange(N):
		line = map(int, raw_input().split(' '))
		inherit.append(line[1:])
	
	print("Case #" + str(i+1) + ":"),
	flag = False
	for j in xrange(N):
		r2d2 = []
		for k in xrange(len(inherit[j])):
			reachable = []
			element = inherit[j][k]
			reachable.append(element)
			to_visit = [element]
			
			while True:
				if to_visit:
					line = to_visit.pop()
					for m in xrange(len(inherit[line-1])):
						to_visit.append(inherit[line-1][m])
						reachable.append(inherit[line-1][m])
				else:
					break
			
			r2d2.append(reachable)
		
		list_of_vals = []
		for x in xrange(len(r2d2)):
			for y in xrange(len(r2d2[x])):
				ele = r2d2[x][y]
				if ele in list_of_vals:
					flag = True
					print("Yes")
					break
				else:
					list_of_vals.append(ele)
			if flag == True:
				break
		if flag == True:
			break
			
					
	if flag == False:
		print("No")
