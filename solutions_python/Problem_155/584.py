

def number_of_friends(shyness):
	shyness_numbers = [int(s) for s in shyness]
	total = shyness_numbers[0]
	to_add = 0
	for i in range(1, len(shyness)):
		if total < i:
			to_add += (i-total)
			total += (i-total) + shyness_numbers[i]
		else:
			total += shyness_numbers[i]
	return to_add

def solve(testid):
	f = open(testid + '.in')
	g = open(testid + '.out', 'w')

	T = int(f.readline())

	for i in range(1,T+1):
		shyness = f.readline().split()[1]
		n = number_of_friends(shyness)
		print i, n

		g.write('Case #{}: {}\n'.format(i, n))

	f.close()
	g.close()

if __name__ == '__main__':
#	solve('A-sample')
#	solve('A-small-attempt0')
	solve('A-large')

