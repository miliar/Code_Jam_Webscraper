def is_tidy(num):
	p = [int(x) for x in list(str(num))]
	for i in range(len(p) - 1):
		if p[i] > p[i+1]:
			return False
	return True

def make_tidy(num):
	p = [int(x) for x in list(str(num))]
	if not is_tidy(num):
		i = 0
		stay = 0
		while i < len(p):
			if p[stay] < p[i]:
				stay = i
				i += 1
			elif p[stay] == p[i]:
				i += 1
			elif p[stay] > p[i]:
				p[stay] = p[stay] - 1
				break
		for j in range(stay + 1, len(p)):
			p[j] = 9
	joined = ''.join([str(x) for x in p])
	return int(joined)

# f = open('b-sample.txt')
f = open('B-large.in')
g = open('b.txt', 'w')

num_test_cases = int(f.readline())

for test_case in range(1, num_test_cases + 1):
	given = f.readline().strip()	
	n = int(given)
	answer = make_tidy(n)
	# final output
	g.write('Case #' + str(test_case) + ': ' + str(answer) + '\n')

g.close()
f.close()