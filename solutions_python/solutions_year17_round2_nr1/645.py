t = int(input())
for testcase in range(1, t + 1):
	line = input().split(" ")
	D = int(line[0])
	N = int(line[1])
	longest_time = 0.0
	for i in range(0, N):
		line2 = input().split(" ")
		Ki = int(line2[0])
		Si = int(line2[1])
		time_i = (D - Ki) / Si
		if time_i > longest_time:
			longest_time = time_i
	
	print("Case #{}: {:.6f}".format(testcase, D / longest_time))

		
'''

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
'''