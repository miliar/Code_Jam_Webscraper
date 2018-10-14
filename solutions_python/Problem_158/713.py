data = '''64
2 2 2
2 1 3
4 4 1
3 2 3
3 1 1
2 1 2
4 2 2
1 1 1
4 3 4
3 3 4
1 1 3
4 1 1
4 4 4
4 2 3
4 2 1
3 1 2
2 3 2
1 4 2
1 2 2
2 4 1
4 1 3
2 1 1
3 3 3
1 3 2
3 4 1
1 3 1
1 2 1
3 2 1
1 1 2
3 2 4
3 1 3
2 3 4
2 3 1
4 3 2
3 4 2
2 4 3
4 4 3
1 2 4
4 1 2
3 4 3
4 3 1
2 2 3
2 1 4
2 4 2
1 4 4
4 1 4
4 4 2
2 4 4
3 2 2
2 2 1
3 3 2
1 2 3
1 1 4
4 2 4
2 3 3
1 3 4
4 3 3
1 4 1
3 1 4
1 3 3
2 2 4
3 3 1
3 4 4
1 4 3
'''
outstore = []

data = [x for x in data.split('\n') if x]

case_count,data = data[0],data[1:]
for case in range(int(case_count)):
	area,row,col = map(int, data[0].split())
	data = data[1:]
	row,col = sorted([row,col])
	impossible = False
	
	if not ((row*col) % area) == 0:
		impossible = True
	if area == 4:
		if col <= 3:
			impossible = True
		elif row <= 2:
			impossible = True
	elif area == 3:
		if col < 3:
			impossible = True
		elif row < 2:
			impossible = True
	case_result = 'Case #%d: '%(case + 1) + ('RICHARD' if impossible else 'GABRIEL')
	print case_result
	outstore.append(case_result)



	




with open('output4.out','w') as f:
	for line in outstore:
		f.write(line+'\n')




