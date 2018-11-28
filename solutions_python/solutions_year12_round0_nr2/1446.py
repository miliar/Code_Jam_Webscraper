f = open('B.in', "r")
res = open('B.txt', "w")
T = int(f.readline())
for line in xrange(0,T):
	s = f.readline()
	numbers = s.split()
	N, S, p = int(numbers[0]), int(numbers[1]), int(numbers[2])
	good, surprising = 0, 0
	for i in xrange(0,N):
		t = int(numbers[3 + i])
		
		if t >= max(3*p - 2, p):
			good = good + 1
		else:
			if t >= max(3*p - 4, p):
				surprising = surprising + 1
	
	answer = good + min(surprising, S)
	res.write('Case #' + str(line + 1) + ': ' + str(answer) + '\n')

