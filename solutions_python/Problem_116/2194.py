#!/usr/bin/python

try:
	input=raw_input
except NameError:
	foo = 1

T = int(input(""))
t = 1
while t <= T :
	r1 = (input(''))
	r2 = (input(''))
	r3 = (input(''))
	r4 = (input(''))
	jnk = input()
	foo = [r1,r2,r3,r4]
	x=0
	y=0
	
	result = ''
	while y < 4:
		tmp = foo[y].replace('T','X')
		if tmp == 'XXXX':
			result = 'X won'
			break;
		tmp = foo[y].replace('T','O')
		if tmp == 'OOOO':
			result = 'O won'
			break
		y = y+1
	
	if result == '':
		while x < 4:
			tmp = (r1[x]+r2[x]+r3[x]+r4[x]).replace('T','X')
			if tmp == 'XXXX':
				result = 'X won'
				break
			
			tmp = (r1[x]+r2[x]+r3[x]+r4[x]).replace('T','O')
			if tmp == 'OOOO':
				result = 'O won'
				break

			x = x + 1
	#/if
	
	if result == '':
		tmp = ''
		x = 0
		while x < 4:
			tmp = tmp + foo[x][x]
			x = x+1
		tmp1 = tmp
		tmp1 = tmp1.replace('T', 'X')
		if tmp1 == 'XXXX':
			result = 'X won'

		tmp = tmp.replace('T','O')
		if tmp == 'OOOO':
			result = 'O won'
	
	if result =='':
			x = 0
			tmp = ''
			while x < 4:
				tmp = tmp + foo[x][4 - x - 1]
				x = x + 1
			
			tmp1 = tmp
			tmp1 = tmp1.replace('T','X')
			if tmp1 == 'XXXX':
				result = 'X won'
			tmp = tmp.replace('T','O')
			if tmp == 'OOOO':
				result = 'O won'

	if result == '':
		tmp = ''
		x = 0
		while x < 4:
			tmp = tmp + foo[x]
			x = x +1
		if not '.' in tmp:
			result = 'Draw'
		else:
			result = 'Game has not completed'

	print 'Case #{0}: {1}'.format(t, result)
	t = t + 1
	#/while
#done
