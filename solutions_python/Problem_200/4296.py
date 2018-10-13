# method to return lastmismatch
def lastMismatch( digits ):
	to_add = 0

	# find no. of digits
	digit_count = len(digits)
	# remove trailing zeros
	# ONLY 1 ZERO
	if digits[digit_count-1] == "0":
		digits = digits[:digit_count-1]
		digit_count -= 1
		to_add += 1	

	# for all the digits
	
	for i in range(digit_count-1):
		last 		 = digits[digit_count-1-i]
		last_but_not = digits[digit_count-1-i-1]
		
		if last < last_but_not : return to_add+1
		elif last == "0": to_add += 1

	# return digit_count as no mismatch
	return to_add

def getAnswer(user_input):

	to_add = lastMismatch(user_input)

	if to_add == 0 : 

		return int(user_input)-1

	else:
		
		less = False
		if user_input[len(user_input)-1] == "0":
			less = True
		# remove to_add number of digits
		user_input = user_input[:-to_add]
		

		suffix = ""
		digit_count = len(user_input)
		rev_num = user_input[::-1]
		
		i=0
		while i<digit_count:
			
			if int(rev_num[i]) != 1:
				break
			i+=1
			suffix += "9"
		
		if i != 0:
			user_input = user_input[:-i]

		
		# if user_input=="":
		for nine in range(to_add):
			suffix += "9"
		if less:
			suffix = suffix[0:-1]
		if user_input != "":
			return str(int(user_input)-1) + suffix
		else:
			return suffix


# read test case
T = int(raw_input())

# for all test cases
for i in range(T):
	# read a number
	 user_input = raw_input()

	 print "Case #"+str(i+1)+": "+getAnswer(user_input)