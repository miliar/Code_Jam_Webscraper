def last_tidy(list_num):
	same = False
	sameIdx = -1
	for idx in range(len(list_num) - 1, 0, -1):
		cn = list_num[idx]
		nn = list_num[idx - 1]

		if (nn > cn):
			"""if same:
				for j in range(idx, sameIdx + 1):
					list_num[j] = 9
				same = False	
			else:
				list_num[idx] = 9
			"""
			for j in range(idx, len(list_num)):
				list_num[j] = 9
			list_num[idx - 1] = nn - 1
		elif (nn == cn):
			if not (same):
				sameIdx = idx
			same = True	

	if (list_num[0] == 0 and len(list_num) > 1):
		return ''.join(map(str, list_num[1:]))
	else:
		return ''.join(map(str, list_num))

def main():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
	  n = [int(s) for s in input()]
	  answer = last_tidy(n)
	  print("Case #{}: {}".format(i, answer))
	  # check out .format's specification for more formatting options
	 

if __name__ == '__main__':
	main()