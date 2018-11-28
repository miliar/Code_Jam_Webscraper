# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	s = str(input().strip())  # read a list of integers, 2 in this case

	last_equal_ind = -1
	ind = 1
	l = len(s)
	while ind < l:
		if s[ind-1] < s[ind]:
			last_equal_ind = -1
		elif s[ind-1] == s[ind]:
			if last_equal_ind == -1:
				last_equal_ind = ind
		else:
			break
		ind += 1
	new_s = ""
	# print("s={}, ind={}, last_equal_ind={}, l={}".format(s, ind, last_equal_ind, l))
	if ind != l:
		if last_equal_ind == -1:
			c = s[ind-1]
			new_s = s[:ind-1] + chr(ord(c)-1) + "9" * (l-ind)
		else:
			c = s[last_equal_ind-1]
			new_s = s[:last_equal_ind-1] + chr(ord(c)-1) + "9" * (l-last_equal_ind)
	else:
		new_s = s

	if new_s[0] == "0":
		new_s = new_s[1:]

	print("Case #{}: {}".format(i, new_s))
	# check out .format's specification for more formatting options
