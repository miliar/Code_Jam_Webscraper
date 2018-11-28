f = open('A-small-attempt0(1).in')

numbers_input = f.readline().split(' ')
T = int(numbers_input[0])

for i in range(T):
	num_str = f.readline().rstrip().split(' ')
	r = int(num_str[0])
	t = int(num_str[1])
	b = r
	c = t
	n = (-b + 0.5 + (b**2 - 2*b*0.5 + 0.25 + 2*c)**0.5)/2
	print('Case #%d: %d' % (i + 1, n))