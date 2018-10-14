testCases = int(input())

for case in range(0, testCases):
	N = input()
	keepGoing = False
	while True:
		keepGoing = False
		for i in range(0, len(N) - 1):
			if int(N[i]) > int(N[i + 1]):
				N = str(N[:i]) + str(int(N[i]) - 1) + '9' * (len(N) - 1 - i)
				keepGoing = True
		if not keepGoing:
			break
	while N[0] == "0":
		N = N[1:]
	print('Case #{}: {}'.format(case + 1, ''.join(N)))
              
