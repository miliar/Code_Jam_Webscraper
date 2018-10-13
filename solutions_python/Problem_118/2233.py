#!/usr/bin/python
import math

def palindrome(i):
	if i % 10 == 0:
		return False
	if i < 10:
		return True
	s = str(i)
	a = list(s)
	b = list(s)
	a.reverse()
	if a == b :
		return True
	return False

def process_line(floor, ceil, T):
	counter = 0
	start = math.ceil(math.sqrt(floor))
	start = int(start)
	while(1):
		if palindrome(start):
			i =int(math.pow(start, 2))
			if i > ceil:
				break
			if i >= floor:
				if palindrome(i):
					counter = counter + 1
		start = start + 1
	return 'Case #%d: %d\r\n' % (T,counter)
	
def main():
	i_file = open('google_q2.txt', 'r')
	o_file = open('google_q2_out.txt', 'w')
	T = int(i_file.readline().split()[0])
	for i in range(T):
		line = i_file.readline().split()
		int_line = map(int, list(line))
		s = process_line(int_line[0],int_line[1] , i+1)
		o_file.write(s)
		
	i_file.close()
	o_file.close()
	print 'End'
	
if __name__ == "__main__":
    main()