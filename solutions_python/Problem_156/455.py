f = open('B-large.in', 'r')
o = open('pancake.out', 'w')

T = int(f.readline().strip('\n'))

for _ in range(T):
	D = int(f.readline().strip('\n'))
	P = map(int, f.readline().strip('\n').split(' '))
	P.sort()
	possible_times = []
	for i in range(1, P[D-1]+1):
		time_i = i
		for x in P:
			if x > i:
				if x % i == 0:
					time_i += x/i-1
				else:
					time_i += x/i
		possible_times.append(time_i)
	result = min(possible_times)
	o.write('Case #' + str(_+1) + ': ' + str(result) + '\n')