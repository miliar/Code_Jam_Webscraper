t = int(raw_input().strip())
t_pointer = 1
while t_pointer <= t:
	node_list = list()
	n = int(raw_input().strip())
	n_pointer = 0
	while n_pointer < n:
		node_list.append([int(node) for node in raw_input().strip().split()[1:]])
		n_pointer += 1
	ans = 'No'
	n_pointer = 1
	while n_pointer <= n and ans != 'Yes':
		visited = list()
		lookup_list = list()
		visited.append(n_pointer)
		lookup_list = node_list[n_pointer - 1]
		while len(lookup_list) > 0:
			node = lookup_list[0]
			lookup_list = lookup_list[1:]
			if node in visited:
				ans = 'Yes'
				break
			else:
				visited.append(node)
				lookup_list.extend(node_list[node - 1])
		n_pointer += 1
	print 'Case #%d: %s' % (t_pointer, ans,)
	t_pointer += 1

