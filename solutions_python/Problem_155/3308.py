import fileinput

def solve(s_max, shyness):
	sum = 0
	count = 0
	added = 0
	diff = 0
	for digit in shyness:
		if sum >= count:
			sum += int(digit)
		else:
			added += (count - sum)
			sum = count
			sum += int(digit)
		count += 1
	return added
		
count = 1
for line in fileinput.input():
	if fileinput.isfirstline():
		continue
	input = line.split()
	ans = solve(input[0], input[1])
	print 'Case #{}: {}'.format(count, ans)
	count += 1