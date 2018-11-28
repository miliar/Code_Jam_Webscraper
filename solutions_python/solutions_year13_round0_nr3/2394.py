import sys

def palindrome(s):
	return s == s[::-1]

def square(i):
	for x in range (1, i+1):
		if (x*x == i):
			return x
			
	return 0
	
out_file = open('output.out', 'w+')
in_file = open('C-small-attempt0.in.txt', 'r+')
num_cases = int(in_file.readline())

for c in range(1, num_cases+1):
	line = in_file.readline().strip('\n').split()
	
	count = 0
	
	for x in range(int(line[0]), int(line[1])+1):
	
		if (palindrome(str(x))):
			
			squaren = square(int(x))
			
			if (squaren != 0):
				if (palindrome(str(squaren))):
					count += 1
					
	case = 'Case #'+str(c)+': ' + str(count)
	out_file.write(case+'\n')