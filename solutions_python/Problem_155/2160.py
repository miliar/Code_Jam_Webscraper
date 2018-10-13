def standing_ovation(s_max, s_list, case_num):
	acc = 0
	min_friend = 0

	for shyness in range(0, s_max+1):
		# print("shyness lv: %d, acc = %d, min friend = %d" % (shyness, acc, min_friend))
		if (shyness > acc and s_list[shyness] != 0):
			min_friend += shyness - acc
			acc += shyness - acc
		acc += s_list[shyness]

	print("Case #%d: %d" % (case_num, min_friend))


def main():
	num_of_case = int(input())
	s_input = []
	for x in range(1, num_of_case+1):
		s_max, s_list = input().split(' ')
		s_max = int(s_max)
		s_list = list(map(int, list(s_list)))
		s_input.append({'s_max' : s_max, 's_list' : s_list, 'case_num' : x})

	for x in range(0, num_of_case):
		standing_ovation(**s_input[x])


if __name__ == '__main__':
	main()