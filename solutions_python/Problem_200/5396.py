import math


def is_tidy(num, lower_bound):
	if len(num) == 0:
		return True
	for el in num:
		if el < lower_bound:
			return False
		lower_bound = el
	return True

def largest_of_length(n):
	return [9]*n

def find_first(num):
	idx = -1
	for i in range(1, len(num)):
		if num[i] < num[i-1]:
			idx = i-1
			break

	if idx == -1:
		return num

	if idx == 0:
		return [num[0]-1] + [9]*(len(num)-1)


	l_idx = idx-1
	while l_idx >= 0 and num[l_idx] > num[idx]-1:
		l_idx -= 1

	if l_idx == -1:
		return [num[0]-1] + [9]*(len(num)-1)

	return num[:l_idx+1] + [num[idx]-1]*(idx-l_idx) + [9]*(len(num)-idx-1)

		


def convert_to_list(n):
	ret = []
	while n > 0:
		ret.append(n % 10)
		n = int(n / 10)
	return [ret[x] for x in range(len(ret)-1, -1, -1)]

def reverse_list(l):
	ret = []
	for idx in range(len(l)-1, -1, -1):
		ret.append(l[idx])
	return ret

def solve(n):
	num = reverse_list(find_first(convert_to_list(n)))

	fin_ans = 0
	last_pow = 1

	for el in num:
		fin_ans += el*last_pow
		last_pow *= 10

	return fin_ans

def main():
	f = open("test_small.in", "r")
	lines = f.readlines()
	t = int(lines[0].rstrip('\n'))

	for case in range(t):
		sol = solve(int(lines[case+1].rstrip('\n')))
		print("Case #%d: %d" %(case+1, sol))

if __name__ == "__main__":
	# f = open("testcase.in", "r")
	main()