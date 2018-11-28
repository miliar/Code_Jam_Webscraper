import sys
import codecs

def main():
	count = 0

	infile = open(sys.argv[1], 'r')
	
	num_testcases = int(infile.readline().rstrip())

	contents = infile.read()
	infile.close()
	cases = contents.split('\n')
	#print(cases)
	
	while (count < num_testcases):
		outfile = open(sys.argv[2], 'w')
		
		for line in cases:
			if (len(line) > 0):
				#print('Starting case')
				result = checkFromInt(line)
				#print(result)
				outfile.write('Case #' + str(count+1) + ': ' + result + '\n')
				count += 1
			
def checkFromInt(str_number):
	#print('checkFromInt(' + str_number + ')')
	number = int(str_number)
	while (not isTidy(str_number)):
		number -= 1
		str_number = str(number)
	return str_number
			
def isTidy(str_number):
	current_lowest = 0
	
	for letter in str_number:
		digit = int(letter)
		if (digit >= current_lowest):
			current_lowest = digit
		else:
			return False
	return True
		
if __name__ =='__main__':main()