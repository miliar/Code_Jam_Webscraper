import sys

import sys

def find_num(num_str):
	list_num = [int(n) for n in list(num_str)]
	brk = -1
	for i in range(len(list_num) - 1):
		if list_num[i] > list_num[i+1]:
			brk = i
			break
	if brk == -1:
		return num_str

	#not tidy
	if brk == 0:
		list_num[i] -= 1

	for i in range(brk, 0, -1):
		list_num[i] -= 1
		if list_num[i-1] <= list_num[i]:
			break
		else:
			list_num[i] = 9
			list_num[i-1] -= 1

	for i in range(brk + 1, len(list_num)):
		list_num[i] = 9

	ret = ''.join([str(x) for x in list_num])

	return ret if ret[0] != '0' else ret[1:]



def tidy(file_name):
	test_count = 0
	with open(file_name,'r') as infile:
		test_count = int(infile.readline())
		for i in range(test_count):
			test_line = infile.readline()
			sol = find_num(test_line[:-1])
			print("case #" + str(i + 1) + ": " + str(sol))


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("usage: ProblemB file_name")
	tidy(sys.argv[1])