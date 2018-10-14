# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import queue

def getOutput(n, k):

	big_current_val = n
	big_current_num = 1
	small_current_val = 0
	small_current_num = 0

	big_sub_count = 0
	small_sub_count = 0
	big_sub = 0
	small_sub = 0

	i = 0
	while i < k:

		if big_current_num > 0:
			current_val = big_current_val
			source = 1 # label current val is from big or small
			big_current_num -= 1
		elif small_current_num > 0:
			current_val = small_current_val
			source = 0
			small_current_num -= 1
		else:
			big_current_val = big_sub
			big_current_num = big_sub_count
			small_current_val = small_sub
			small_current_num = small_sub_count
			big_sub_count = 0
			small_sub_count = 0
			big_sub = 0
			small_sub = 0
			continue

		if current_val % 2 == 0:
			big_sub = current_val//2
			small_sub = current_val//2 - 1
			big_sub_count += 1
			small_sub_count += 1
		else:
			if source == 1:
				big_sub = current_val//2
				big_sub_count += 2
			else:
				small_sub = current_val//2
				small_sub_count += 2
		# print(str(i)+":"+str(current_val))
		# print(str(i)+":"+str(big_sub_count))
		# print(str(i)+":"+str(small_sub_count))
		i += 1

	# if current_num == 0:
	# 	return 0, 0
	if current_val % 2 == 0:
		return current_val//2, current_val//2 - 1
	else:
		return current_val//2, current_val//2

if __name__ == '__main__':
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
	  n, k = [input_line for input_line in input().split(" ")]  # read a list of integers, 2 in this case
	  max_value, min_value = getOutput(int(n), int(k))
	  print("Case #{}: {} {}".format(i, max_value, min_value))
	  # check out .format's specification for more formatting options