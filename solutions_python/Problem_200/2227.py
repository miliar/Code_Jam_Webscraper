testfile = open('B-large.in', 'r')
outfile = open('output.txt', 'w')

def get_highest_tidy(N):
	current = N[0]
	i_current = 0
	for i in range(len(N) - 1):
		if current < N[i]:
			current = N[i]
			i_current = i
		if(N[i] > N[i + 1]):
			# N[i] = str(int(N[i]) - 1)
			N[i_current] = str(int(N[i_current]) - 1)
			# for j in range(i + 1, len(N)):
				# N[j] = '9'
			for j in range(i_current + 1, len(N)):
				N[j] = '9'
	return int(''.join(N))

def main():
	test_cases = int(testfile.readline().strip())
	for i in range(test_cases):
		num = list(testfile.readline().strip())
		last_tidy = get_highest_tidy(num)
		outfile.write('Case #' + str(i + 1) + ': ' + str(last_tidy))
		if(i + 1 < test_cases):
			outfile.write('\n')

main()