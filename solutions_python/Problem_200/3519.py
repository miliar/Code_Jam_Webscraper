def check_max_tidy_num(max_num):
	if max_num == '0':
		return ''
	if len(max_num) == 1:
		return max_num
	result = int(max_num[0])
	for i in range(1, len(max_num)):
		digit = int(max_num[i])
		if digit < result % 10:
			return check_max_tidy_num(str(result - 1)) + '9' * (len(max_num) - i)
		else:
			result = result * 10 + digit
	return str(result)

file = "B-large.in.txt"
output = open("PB-large-ouput.txt", 'w')
f = open(file, 'r')
T = int(f.readline().strip())

for i in range(T):
	num = f.readline().strip()
	result = check_max_tidy_num(num)
	output.write("Case #%d: %s\n" % (i+1, result))

f.close()
output.close()