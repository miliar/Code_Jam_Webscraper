import math
import sys

def main():
	file_read = open(sys.argv[1], 'r')
	lines = file_read.readlines()	
	no_test_cases = int(lines[0])
	for k in range(no_test_cases):		
		input = lines[k+1].split()
		limits = [] ; output = []
		limits.append(int(input[0]))
		limits.append(int(input[1]))
		for num in range(limits[0], (limits[1]+1)):
			str_rep = str(num)
			for j in range(len(str_rep)-1, 0, -1):
				if int(str_rep[j:]+str_rep[:j]) >= limits[0] and int(str_rep[j:]+str_rep[:j]) <= limits[1]:
					pair = [num, int(str_rep[j:]+str_rep[:j])]
					pair.sort()
					if pair not in output and pair[0] != pair[1]:
						output.append(pair)
		
		print "Case #" + str(k+1) + ":",
		print len(output)
		

if __name__ == '__main__':
	main()