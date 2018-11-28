
def last_tidy_num(num):

	num_current = num
	while num_current > 0:
		num_str = str(num_current)
		#print(num_str)

		if len(num_str) <= 1:
			return num_current

		goNext = False
		for j in range(len(num_str) - 1):
			#print("comparing {} and {}".format(num_str[j], num_str[j+1]))
			if num_str[j] > num_str[j+1]:
				goNext = True
				num_current = int(num_str[:j+1]) * (10 ** len(num_str[j+1:]))
				break

		if goNext == True:
			num_current -= 1
			continue

		return num_current

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  num = int(input())
  ans = last_tidy_num(num)
  print("Case #{}: {}".format(i, ans))