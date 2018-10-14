def is_tidy(string):
	num_list = list(map(int,string))
	sorted_list = list(num_list)
	sorted_list.sort()
	return num_list == sorted_list

def find_last_tidy(num):
	while num > 0:
		if is_tidy(str(num)):
			return num
		num -= 1

def find_last_tidy_fast(num):
	if is_tidy(str(num)):
		return num
	digits = len(str(num))
	for i in range (0,digits):
		digit = int(str(num)[digits - i - 1])
		value = 10 ** i
		num -= (digit+1)*value
		if is_tidy(str(num)):
			return num


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  test_case = int(input())
  print("Case #{}: {}".format(i, find_last_tidy_fast(test_case)))

#print (is_tidy('132'))
#print (is_tidy('129'))
#print (is_tidy('1000'))
#print (is_tidy('7'))
#print (is_tidy('11111'))
#print (is_tidy('1224'))
#print (find_last_tidy_fast(132))
#print (find_last_tidy_fast(1000))
#print (find_last_tidy_fast(1230567))
#print (find_last_tidy_fast(111111111111111110))
#print (find_last_tidy(1230567), find_last_tidy_fast(1230567))
#print (find_last_tidy(23298), find_last_tidy_fast(23298))
#print (find_last_tidy(23829), find_last_tidy_fast(23829))
#print (find_last_tidy(1209), find_last_tidy_fast(1209))
#print (find_last_tidy(92382), find_last_tidy_fast(92382))