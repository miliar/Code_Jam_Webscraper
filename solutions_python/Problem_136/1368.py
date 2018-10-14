#!/usr/bin/python 

import sys
def RF(numbers_str):
	return [float(x) for x in numbers_str]
def Clicker(C,F,X):
	s = 2.0
	t = 0.0
	while X/s > C/s + X/(s+F) :
		t+= C/s
		s+=F
	t += X/s
	return t

def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		
		s = sys.stdin.readline()
		numbers_str = s.split()
		res = Clicker(float(numbers_str[0]),float(numbers_str[1]),float(numbers_str[2]))
		sys.stdout.write('Case #{}: '.format(i+1))
		sys.stdout.write('%f\n' %res)
        # print "%.2f kg = %.2f lb = %.2f gal = %.2f l" % (var1, var2, var3, var4)
        #print "%f\n" %(res)
        
        #convert numbers to floats
        #nums = [float(x) for x in numbers_str]
        #nums = RF(numbers_str)
        #print "HERE3"
        #res = Clicker(nums[0],nums[1],nums[2])
        
        

if __name__ == '__main__':
	main()
