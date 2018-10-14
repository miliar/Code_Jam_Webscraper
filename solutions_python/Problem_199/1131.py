t = int(input())
for testcase in range(1, t + 1):
	line = input().split(" ")
	s = list(line[0])
	s_length = len(s)
	flipper_size = int(line[1])
	
	#storage = [[0]*(s_length - flipper_size)]*(s_length - flipper_size)
	flips = 0
	for i in range(0, s_length - flipper_size + 1):
		if s[i] == '-':
			flips += 1
			for j in range(i, i + flipper_size):
				if s[j] == '-':
					s[j] = '+'
				else:
					s[j] = '-'
	valid = True
	for i in range(s_length - flipper_size + 1, s_length):
		if s[i] == '-':
			valid = False
			break
	if valid:
		print("Case #{}: {}".format(testcase, flips))
	else:
		print("Case #{}: IMPOSSIBLE".format(testcase))
