


def solve(cake, kids):
	for i in range(len(cake)):
		row = cake[i]
		cur = None
		for cell in row:
			if cell != '?':
				cur = cell
				break
		if cur == None:
			continue
		for j in range(len(row)):
			if row[j] == '?':
				row[j] = cur
			else:
				cur = row[j]
	
	cur_row = None
	
	
	
	for i in range(len(cake)):
		row = cake[i]
		if row[0] != '?':
			cur_row = row
			break
		
	for i in range(len(cake)):
		row = cake[i]
		if row[0] == '?':
			for j in range(len(row)):
				row[j] = cur_row[j]
		else:
			cur_row = row
		
	print
	print '\n'.join(''.join(row) for row in cake)
			

case_count = input()
for case in range(1,case_count+1):
	print 'Case #%d:' % case,
	r,c = map(int,raw_input().split(' '))
	cake = []
	for _ in range(r):
		cake.append(list(raw_input()))
	kids = set(c for row in cake for c in row)
	kids.discard('?')
	solve(cake, kids)