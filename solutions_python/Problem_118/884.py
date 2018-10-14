import sys

input_list = []
output_list = []

def trans_code(org_num, from_digit, to_digit):
	org_num = str(org_num)
	org_value = 0
	from_digit = int(from_digit)
	to_digit = int(to_digit)
	result = ''
	for x in range(len(org_num)):
		org_value += int(org_num[x]) * (from_digit ** (len(org_num)-x-1))
	while True:
		dummy_digit = org_value % to_digit
		result = str(dummy_digit) + result
		org_value = (org_value - dummy_digit)/to_digit
		if org_value < to_digit:
			result = str(org_value) + result
			break
	return long(result)

def is_pal(num):
	str_num = str(num)
	if len(str_num)%2 == 0:
		for x in range(len(str_num)/2):
				if str_num[x] != str_num[len(str_num)-x-1]:
					return False
	else:
		for x in range((len(str_num)-1)/2):
			if str_num[x] != str_num[len(str_num)-x-1]:
				return False
	return True

def reverse_str(str_org):
	str_dummy = ''
	str_org = str(str_org)
	for x in range(len(str_org)):
		str_dummy = str_org[x] + str_dummy
	return str_dummy

def next_seed_num(num):
#	print num
	str_num = str(num)
	str_num_next = trans_code(trans_code(str_num, 4, 10)+1, 10, 4)
	return str_num_next

def pal_list():
	total_len = 2
	max_total_len = 15
	seed_num = 1
	result = []
	while total_len <= max_total_len:
#		print seed_num, result, total_len
		if total_len % 2 == 0:
			dummy_str = str(seed_num) + reverse_str(seed_num)
			if is_pal(long(dummy_str) ** 2):
				result.append(long(dummy_str))
		else:
			for x in range(3):
				dummy_str = str(seed_num) + str(x) + reverse_str(seed_num)
				if is_pal(long(dummy_str) ** 2):
					result.append(long(dummy_str))
		
		next_seed = next_seed_num(seed_num)
#		print 'seed', seed_num, 'next', next_seed
		if len(str(next_seed)) > len(str(seed_num)):
			if total_len % 2 == 0:
				seed_num = next_seed / 10
				total_len += 1
			else:
				seed_num = next_seed
				total_len += 1
		else:
			seed_num = next_seed
	return result

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_count = 0
	for input_line in input_lines:
		input_split = input_line.split()
		if len(input_split) > 1:
			input_split[0] = int(input_split[0])
			input_split[1] = int(input_split[1])
		input_list.append(input_split)
	input_f.close()
except:
	print 'read error'
	exit()

input_list.pop(0)

pal_list = pal_list()
pal_list.insert(0, 3)
pal_list.insert(0, 2)
pal_list.insert(0, 1)
#print pal_list
#exit()
for input_line in input_list:
	result = 0
	for x in pal_list:
		if x < (input_line[0] ** 0.5):
			continue
		if x > (input_line[1] ** 0.5):
			break
		result += 1
	output_list.append([result])

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
