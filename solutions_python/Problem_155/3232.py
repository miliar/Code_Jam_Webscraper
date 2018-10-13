import sys

f = open(sys.argv[1])
f2 = open(sys.argv[2], 'w')
test_case = int(f.readline().strip())
case = 1
for line in f:
	parse = line.strip('\n').split()
	max_shy = int(parse[0])
	friends = 0
	counter = 1
	digits = parse[1]
	number = 0
	for i in range(0, len(digits)):
		number += int(digits[i])
		if number < counter:
			
			friends += counter-number
			number += counter-number
		counter += 1
	f2.write('Case #%d: %d\n' % (case, friends))
	case+= 1


