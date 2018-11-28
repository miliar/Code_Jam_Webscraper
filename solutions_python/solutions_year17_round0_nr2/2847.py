# your code goes here
import sys

def check_tidy(number):
	num_copy = number
	str_num = str(number)
	# print "Check #"+ str(count)+ ": " + str_num
	num_len = len(str_num)
	try:
		for num in range(num_len - 1):
			if str_num[num] <= str_num[num+1]:
				# print str_num[num] + " <=" + str_num[num+1]
				pass
			else:
				# print str_num[num] + " > " + str_num[num+1]
				# Now we know that the number next to it is greater
				# as soon as we figure that out we must find the index of the
				# same number in the string
				num_index = str_num.find(str_num[num])
				sub_num = str_num[num_index+1:]
				# print "index of less int: " + str(num_index) + " and the number is: " + str_num[num]
				# print "sub_num: " + sub_num
				pre_tidy = number - int(sub_num)
				pre_tidy -= 1
				str_num = str(pre_tidy)
				# print "pretidy: " + str(pre_tidy)
				tidy_number = number - 10**num
	except:
		pass

	print "Case #"+ str(count)+ ": " + str_num

count = 0
for line in sys.stdin:
    if count == 0:
    	num_tests = int(line)
    	# print "num_tests: " + str(num_tests)
    	count += 1
    else:
    	number = int(line)
    	# print "number: " + str(number)
    	check_tidy(number)
    	count += 1
