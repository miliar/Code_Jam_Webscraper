import sys
import math

# def is_palindrome(s):
# 	s = str(s)
# 	return s == s[::-1]

# t = input()
# for test_case in range(t):
# 	line = raw_input()
# 	inf, sup = line.split(" ")
# 	inf = int(inf)
# 	sup = int(sup)

# 	new_inf = int(math.ceil(math.sqrt(inf)))
# 	new_sup = int(math.floor(math.sqrt(sup)))

# 	count = 0
# 	pre_calculated = []
# 	for i in range(new_inf, new_sup+1):
# 		square = i*i
# 		if is_palindrome(i):
# 			if is_palindrome(square):
# 				count += 1
# 				pre_calculated.append(square)

# 	if test_case == 4:
# 		print pre_calculated
# 	print "Case #" + str(test_case+1) + ": " + str(count)

pre_calculated = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

t = input()
for test_case in range(t):
	line = raw_input()
	inf, sup = line.split(" ")
	inf = int(inf)
	sup = int(sup)

	count = 0
	for pre_calc_value in pre_calculated:
		if pre_calc_value >= inf and pre_calc_value <= sup:
			count += 1

	print "Case #" + str(test_case+1) + ": " + str(count)