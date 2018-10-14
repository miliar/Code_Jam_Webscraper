t = int(raw_input())
for i in xrange(1, t + 1):
	line = raw_input()
	line = line.split(' ')
	n = int(line[0])
	k = int (line[1])
	if n == k:
		print "Case #{}: {} {}".format(i, 0, 0)
	else:
		row = ['o']
		for j in xrange(0, n):
			row.append('.')
		row.append('o')
		mx = 0
		mn = 0
		for p in xrange(0, k):
			stall_set = []
			current = 1
			end = len(row) - 1
			while current < end:
				if row[current] == '.':
					next_empty_count = 0
					ahead = current + 1
					while row[ahead] == '.':
						next_empty_count += 1
						ahead += 1
					prev_empty_count = 0
					prev = current - 1
					while row[prev] == '.':
						prev_empty_count += 1
						prev -= 1
					stall_set.append({
						'set': [prev_empty_count, next_empty_count],
						'index': current
					})
				current += 1
			
			min_set = []
			for item in stall_set:
				min_set.append({
					'min': min(item['set']),
					'index': item['index'],
					'set': item['set']
				})
			seq_min = [x['min'] for x in min_set]
			mn = max(seq_min)
			
			new_min_set = []
			for item in min_set:
				if item['min'] == mn:
					new_min_set.append(item)
			
			max_set = []
			for item in new_min_set:
				max_set.append({
					'max': max(item['set']),
					'index': item['index']
				})
			seq_max = [x['max'] for x in max_set]
			mx = max(seq_max)

			if seq_min.count(mn) == 1:
				for item in new_min_set:
					if item['min'] == mn:
						row[item['index']] = 'o'
						break
			else:
				for item in max_set:
					if item['max'] == mx:
						row[item['index']] = 'o'
						break
		print "Case #{}: {} {}".format(i, mx, mn)