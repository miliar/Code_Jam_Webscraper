t = int(input())
for i in range(1, t + 1):
	result = True
	swap = 0
	line = input().split(" ")
	s = list(line[0])
	k = int(line[1])
	n = len(s)
	for j in range(n - k + 1):
		if s[j] == '-':
			s[j:j+k] = ['+' if item is '-' else '-' for item in s[j:j+k]]
			swap = swap + 1
	for j in range(max(n - k + 1, 0), n):
		if s[j] == '-':
			result = False
			break
	print("Case #{}: {}".format(i, swap)) if result else print("Case #{}: {}".format(i, "IMPOSSIBLE"))