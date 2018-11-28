#!/urs/bin/env python3

with open ('input.txt') as input:
	input.readline()
	case = 0
	for line in input:
		case += 1
		radius, paint = map(int, line.split())
		k = 0
		area = (2*radius+1)
		while(paint>=area):
			k+=1
			paint -= area
			radius += 2
			area = (2*radius+1)
		print('Case #{}: {}'.format(case,k))