#!/usr/bin/python 

import sys
def RF(numbers_str):
	return [float(x) for x in numbers_str]
def DB (A,B,l):
	B.sort()
	A.sort()
	
	for k in range(l) :
		f = True
		for i in range(l-k) :
			if A[i+k] < B[i] :
				f = False
		if f == True:
			return l-k
	return 0
def BB (A,B,l):
	B.sort()
	A.sort()
	c = 0
	for k in range(l) :
		if B[k] < A[k] :
			c+=1
	return c
def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		
		s = sys.stdin.readline()
		numbers_str = s.split()
		l = int(numbers_str[0])
		s = sys.stdin.readline()
		numbers_str = s.split()
		A = RF(numbers_str)
		s = sys.stdin.readline()
		numbers_str = s.split()
		B = RF(numbers_str)
		resd = DB(A,B,l)
		resb = l- DB(B,A,l)		 
		sys.stdout.write('Case #{}: '.format(i+1))
		#print resd
		sys.stdout.write('%d ' %resd)
		sys.stdout.write('%d\n' %resb)
        
        
        

if __name__ == '__main__':
	main()
