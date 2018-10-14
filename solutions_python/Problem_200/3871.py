def tidy(n):
   l = [int(ch) for ch in str(n)]
   length = len(l)
   if length is 1:
       return True, n
   for i in range(length - 1):
       if l[i] > l[i + 1]:
           k = l[:i + 1] + [0] * (length - (i + 1))
           j = (long(''.join([str(i) for i in k])) - 1)
           return False, j
   return True, n

def get_tidy_number(n):
   is_tidy, next_num = tidy(n)
   while not is_tidy:
       is_tidy, next_num = tidy(next_num)
   return next_num

def main():
	output_file = open('output.txt', 'w+')
	for test in range(int(raw_input())):
		input_str = raw_input()
		try:
			input_num = long(input_str)
			tidy_num = get_tidy_number(input_num)
		except:
			tidy_num = input_str  
		string_to_print = "Case #"+str(test+1)+": "+str(tidy_num)
		print string_to_print
		output_file.write( string_to_print + '\n')
	output_file.close()	
	
main()		

