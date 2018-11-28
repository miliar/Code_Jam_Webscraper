#!/urs/bin/env python3
field = []
mins = []

def horizontal(i):
	for a in range(m):
			if field[i][a] > min:
				return 0
	return 1

def vertical(j):
	for a in range(n):
			if field[a][j] > min:
				return 0
	return 1

def test():
	global min, field, mins
	min = 101
	for i in range(n):
		for j in range(m):
			field[i][j] = int(field[i][j])
			if field[i][j] < min:
				min = field[i][j]
	for i in range(n):
		for j in range(m):
			if min == field[i][j]:
				mins.append(tuple([i,j]))
	for x in mins:
		i = x[0]
		j = x[1]
		if not(horizontal(i) or vertical(j)):
			return 0
	return 1	


with open ('input.txt') as input:
	input.readline()
	k = 1
	for line in input:
		n,m = line.split(' ')
		n = int(n)
		m = int(m)
		for i in range(n):
			field.append(input.readline()[:-1].split(' '))
		if test():
			print('Case #{}: YES'.format(k))
			#print(n,m)
		else:
			print('Case #{}: NO'.format(k))
			#print(n,m)
		field = []
		mins = []
		k+=1