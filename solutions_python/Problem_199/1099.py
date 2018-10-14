# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def getOutput(s, k):

	count = 0
	plus_count = 0

	for i in range(len(s)):
		if s[i] == '+':
			plus_count += 1
	if plus_count == len(s):
		return count

	for i in range(len(s)- k + 1):
		if s[i] == '-':
			count += 1
			for j in range(k):
				if s[i+j] == '+':
					s[i+j] = '-'
					plus_count -= 1
				elif s[i+j] == '-':
					s[i+j] = '+'
					plus_count += 1
			if plus_count == len(s):
				return count
	return 'IMPOSSIBLE'

if __name__ == '__main__':
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
	  s, k = [input_line for input_line in input().split(" ")]  # read a list of integers, 2 in this case
	  print("Case #{}: {}".format(i, getOutput(list(s), int(k))))
	  # check out .format's specification for more formatting options