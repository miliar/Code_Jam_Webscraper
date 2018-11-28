def find_add(table, value, num):
	for x in range(len(table)):
		if table[x][0] == value:
			table[x] = (value, table[x][1]+num)
			table.sort(key=lambda tup: tup[0], reverse=True)
			return table
	table.append((value, num))
	table.sort(key=lambda tup: tup[0], reverse=True)
	return table
			
		

T = int(input())
for t in range(T):
	[n, P] = [int(x) for x in input().split()]

	#print(" ---- ")
	#print("{} {}".format(n, P))
	d = [(n, 1)]
	p = 0
	res_min = 0
	res_max = 0
	if n > P:
		while p < P:
			#print(d)
			elem = d[0]
			d = d[1:]
			res = elem[0]-1
			if P-p > elem[1]:
				if res % 2 == 0:
					d = find_add(d, int(res/2), 2*elem[1])
				else:
					d = find_add(d, int(res/2), elem[1])
					d = find_add(d, int(res/2+1), elem[1])
			else:
				if res % 2 == 0:
					res_min = int(res/2)
					res_max = int(res/2)
				else:
					res_min = int(res/2)
					res_max = int(res/2+1)
					
			p = p+elem[1]
	print("Case #{}: {} {}".format(t+1, res_max, res_min))

	
	
