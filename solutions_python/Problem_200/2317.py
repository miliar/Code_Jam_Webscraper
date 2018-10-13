import sys

num_args = int(input())

for case_number in range(0, num_args):
	max_num = list(input())
	
	last = 0
	i = 0
	while i < len(max_num):
		current = int(max_num[i])
		if current >= last:
			last = current
			i += 1
		else:
			break

	if i == len(max_num):
		print("Case #" + str(case_number + 1) + ": " + str(int(''.join(max_num))))
	else:
		to_subtract = max_num[:max_num.index(max_num[i-1]) + 1]
		to_subtract = ''.join(to_subtract[:i])
		to_subtract = int(to_subtract) - 1
		to_subtract = list(str(to_subtract)) + ['9']*len(max_num[max_num.index(max_num[i-1]) + 1:])
		to_subtract = ''.join(to_subtract)

		print("Case #" + str(case_number + 1) + ": " + str(int(to_subtract)))
