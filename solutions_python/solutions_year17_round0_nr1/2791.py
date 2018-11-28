def get_num_flips(string, k):
	num_flips = 0
	for i in range(len(string)-k+1):
		if string[i] == '-':
			num_flips += 1
			for j in range(k):
				if string[i+j] == '-':
					string[i+j] = '+'
				else:
					string[i+j] = '-'
	if all(char == '+' for char in string):
		return num_flips
	else:
		return -1

n = int(input())
for i in range(n):
	string, k = input().split()
	num_flips = get_num_flips([char for char in string], int(k))
	if num_flips == -1:
		print('Case #'+str(i+1)+': IMPOSSIBLE')
	else:
		print('Case #'+str(i+1)+': ' + str(num_flips))

