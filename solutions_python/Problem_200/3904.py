def convert_to_number(number):
    return int(''.join(str(i) for i in number))

def check_lower_numbers(number_list, index):
	number = number_list[index]

	for idx in range(index + 1, len(number_list)):
		if number_list[idx] < number:
			return True
	return False

with open("B-small-attempt1.in") as f:
	content = f.readlines()
content = [x.strip() for x in content] 

num_probs = int(content[0])

for i in range(1, num_probs+1):
	num = int(content[i])
	list_num = [int(d) for d in str(num)]
	last_digit = list_num[0]
	for index in range(1, len(list_num)):
		if last_digit >= list_num[index]:
			if last_digit == list_num[index] and check_lower_numbers(list_num, index) == False:
				continue
			list_num[index-1] = last_digit - 1
			for index2 in range(index, len(list_num)):
				list_num[index2] = 9
			break;
		else:
			last_digit = list_num[index]
	print "Case #{}: {}".format(i, convert_to_number(list_num))

