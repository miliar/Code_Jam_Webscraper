# Tidy Numbers
# Google CodeJam - 2017 - Qualification Round - Problem B

import helper

def check_number(number):
	s_number = str(number)
	l = len(s_number)
	
	for i in range(l-1):
		if i == 0:
			n = s_number[-2:]
		else:
			i *= -1
			n = s_number[i-2:i]
		
		n1 = int(n[0])
		n2 = int(n[1])
		
		if n1 > n2:
			return False
		
	return True

# Redundant, I'm sure there's a better way to do this but without seperating
# the two functions an exponent of 1 would be equivalent to returning True
# which is incorrect...

def get_exp(number):
	s_number = str(number)
	l = len(s_number)
	
	if s_number.rfind("0") != -1:
		if s_number.rfind("0") == l-1:
			return 0
		else:
			return l - s_number.rfind("0") - 2
		
	for i in range(l-1):
		if i == 0:
			n = s_number[-2:]
		else:
			i *= -1
			n = s_number[i-2:i]
		
		n1 = int(n[0])
		n2 = int(n[1])
		
		if n1 > n2:
			return i * -1
		
def main():
	dataset = helper.get_dataset()
	outfile = helper.create_output_file()
	num = 1
	
	for case in dataset:
		n = int(case)
		while True:		
				if check_number(n):
						solution = n
						break
						
				exp = get_exp(n)
				inc = pow(10, exp)
				n -= inc
				
		
		outfile.write("Case #" + str(num) + ": " + str(solution) + "\n")
		
		print "Case #%s: %s" % (num, solution)
		num += 1
	
	outfile.close()
	print "[+] All cases solved!"
	
if __name__=='__main__':
	main()
