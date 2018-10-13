def secondary(c,array):
	i = 0
	j = 3
	flag = 0
	while(i < 4):
		if array[i][j] == c or array[i][j] == 'T':
			i += 1
			j -= 1
			flag = 1
		else:
			flag = 0
			break
	return flag
def along(c,array):
	i = 0
	j = 0
	flag = 0
	while(i<4):
		if array[i][j] == c or array[i][j] == 'T':
			j += 1
			flag = 1 
		else:
			j = 0
			i += 1
			flag = 0
		if j == 4:
			break
	return flag

def down(c,array):
	i = 0
	j = 0
	flag = 0
	while(j<4):
		if array[i][j] == c or array[i][j] == 'T':
			i += 1
			flag = 1
		else:
			i = 0
			j += 1
			flag = 0
		if i == 4:
			break
	return flag

def primary(c,array):
	i = 0
	j = 0
	flag = 0
	while(i<4):
		if array[i][j] == c or array[i][j] == 'T':
			j += 1
			i += 1
			flag = 1
		else:
			flag = 0
			break
	return flag



def case(c,array):
	if along(c,array) == 1 or down(c,array) == 1 or primary(c,array) == 1 or secondary(c,array) == 1:
		return 1
	else:
		return 0

t = int(raw_input())
for i in range(t):
	if i >= 1:
		s = raw_input()
	array = []
	dc = 0
	for j in range(4):
		s = raw_input()
		if s != '\n':
			dc += s.count('.')
			array.append(s)
	if case('X',array)  == 1:
		print "Case #%i: X won"%(i+1)
	elif case('O',array) == 1:
		print "Case #%i: O won"%(i+1)
	elif dc == 0:
		print "Case #%i: Draw"%(i+1)
	else:
		print "Case #%i: Game has not completed"%(i+1)
