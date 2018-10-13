import math
import sys

def main():
	file_name = sys.argv[1]
	input_file = open(file_name, 'r')
	output_file = open('output.o', 'w')
	
	T = int(input_file.readline())
	
	for i in range(T):
		range_values = input_file.readline().split()
		A = int(range_values[0])
		B = int(range_values[1])
		count = 0
		for number in range(A, B + 1):
			if str(number) == str(number)[::-1]:
				if int(math.sqrt(number)) == math.sqrt(number):
					if str(int(math.sqrt(number))) == str(int(math.sqrt(number)))[::-1]:
						count += 1
		output_file.write('Case #%d: %d\n' % (i + 1, count))
	
	output_file.close()
	input_file.close()

if __name__ == '__main__':
	main()
