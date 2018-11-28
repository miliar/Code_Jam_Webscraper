import sys

def get_tidynumber_string(str_num):
	if len(str_num) == 1:
		return str_num
		
	length = len(str_num)
	str_list = list(str_num)
	for i in reversed(range(length)):
		if i > 0:
			if str_list[i] < str_list[i-1]:
				str_list[i] = '9'
				if str_list[i-1] == '0':
					str_list[i-1] = '9'
				else:
					str_list[i-1] = chr(ord(str_list[i-1]) - 1)
					str_list[i:] = '9'*(length-i)
	
	result = ''.join(str_list)
	result = result.strip()
	result = result.lstrip('0')
	return result
	
def main():
	fr = open('B-large.in', 'r')
	#fr = open('tidy_number_small.txt', 'r')
	fw = open('tidy_number_large_answer.txt', 'w')
	
	T = int(fr.readline())
	print( "%d test cases" % T)
	for i in range(T):
		N = str(fr.readline().split()[0])
		print( "input number :" + N)
		
		result = get_tidynumber_string( N )
		
		print("Case #"+str(i+1)+": "+result)
		fw.write("Case #"+str(i+1)+": "+result+"\n")
	fr.close()
	fw.close()

if __name__ == '__main__':
	main()

