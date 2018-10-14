import sys

input = open(sys.argv[1], 'r')

t = int(input.readline())

for i in range(t):
	line = input.readline()
	[c, f, x] = map(float, line.split())
	
	curr_time = -1
	farm_time = 0
	farms = 0
	while (True):
		next_time = farm_time + (x / (2 + (farms * f)))
		if ((curr_time != -1) and (curr_time < next_time)):
			break
		else:
			curr_time = next_time
			farms += 1
			farm_time += (c / (2 + ((farms - 1) * f)))

	sys.stdout.write('Case #' + str(i + 1) + ': ')
	print(round(curr_time, 7))

input.close()
