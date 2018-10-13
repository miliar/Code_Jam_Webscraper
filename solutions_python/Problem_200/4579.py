import sys
# what was the last tidy number?
# 

def parse_input_file(fn):
	with open(fn, "r")  as f:
		lines = f.readlines()

	nbr_inputs = int(lines[0])
	inputs = [int(inp) for inp in (lines[1:])] 
	return inputs

def is_last_tidy_number(n):
	#print 'n = %i' %(n)
	str_n = str(n)

	if len(str_n) == 1:
		return True  # single digit number

	#if (str_n[ind_last_dig] < str_n[ind_last_dig-1]):
	#	find_last_tidy_number(n-1) # n is not the last tidy number

	for digit, i in zip(str_n, range(len(str_n))):
		if i < len(str_n)-1:
			#print 'len = %i' %(len(str_n))
			#print 'i = %i' %(i)
			if str_n[i] > str_n[i+1]: # then we know it is not a tidy number
				return False # we will have to do something different because recursion doesnt work because it causes stack overflow

	return True


def main():
	if len(sys.argv) == 2:
		inputs = parse_input_file(sys.argv[1])

		for inp, i in zip(inputs, range(len(inputs))):
			ltn = inp
			for nb in reversed(range(inp+1)):
				if is_last_tidy_number(nb):
					ltn = nb
					break #??

				else:
					pass
					#print "ww"


			print "Case #%i: %i" %(i+1, ltn)



	else:
		"Nothing is not right. Have you forgetten the input file?"

if __name__ == "__main__":
	main()