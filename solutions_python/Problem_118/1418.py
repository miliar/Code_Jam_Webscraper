import gmpy
import sys


file_string = sys.argv[1]
my_file = open (file_string)
current_line = my_file.readline()
n = int(current_line,10)

def is_palindrome(n):
	m = str(n)
	if len(m) == 1 or len(m) == 0:
		return True
	else:
		new_word = m[1:len(m)-1]
		if m[0] == m[len(m)-1]:
			return is_palindrome(new_word)
		else:
			return False

m = 1

output = 0
while m <= n:
	current_line = my_file.readline()
	start = ""
	end = ""
	space_index = current_line.find(" ")
	start = current_line[0:space_index]
	end = current_line[space_index+1:]

	start_num = int(start, 10)
	end_num = int(end, 10)

	while start_num <= end_num:
		if is_palindrome(start_num) and gmpy.is_square(start_num):
			root = start_num**0.5

			if is_palindrome(str(int(root))):
				output = output + 1
		start_num = start_num + 1
	print "Case #" + str(m) + ": " + str(output)
	output = 0
	m = m+1



