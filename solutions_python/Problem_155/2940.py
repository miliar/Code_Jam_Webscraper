with open('ovation.in') as f:
	lines = f.readlines()

	t = lines[0]
	c = []
	for tc in lines[1:]:
		c += [tc.strip().split(' ')]

	f.close()

f = open('ovation.out', 'r+')

for tc in range(len(c)):
	max_shy = int(c[tc][0])
	num_shy = c[tc][1]

	total_up = 0
	total_needed = 0

	for shy in range(max_shy+1):
		if int(num_shy[shy]) > 0:
			if total_up >= shy:
				total_up += int(num_shy[shy])
			else:
				needed = shy - total_up
				total_needed += needed
				total_up += needed + int(num_shy[shy])
	
	f.write('Case #' + str(tc + 1) + ': ' + str(total_needed) + '\n')