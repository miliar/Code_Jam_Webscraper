# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	s, k = input().split(" ")  # read a list of integers, 2 in this case
	s = [1 if item == '+' else 0 for item in s]
	k = int(k)

	ind = 0
	l = len(s)
	turn_count = 0
	while ind + k - 1< len(s):
		if s[ind]:
			ind += 1
		else:
			for j in range(ind, ind+k):
				s[j] = 1 - s[j]
			ind += 1
			turn_count += 1
	p = True
	while ind < len(s):
		if s[ind] == 0:
			p = False
			break
		ind += 1
	
	if p:
		print("Case #{}: {}".format(i, turn_count))
	else:
		print("Case #{}: {}".format(i, "IMPOSSIBLE"))
	      # check out .format's specification for more formatting options
