#!/usr/bin/python
import sys
import math

def is_palindrome(num):
	n=num
	rev = 0;
	while (num > 0):
		dig = num % 10;
		rev = rev * 10 + dig;
		num = num / 10;
	if(n==rev):
		return True
	else:
		return False

def C():


	
	T = input()
	
	for test_case in range(T):
		cont =0
		limits = raw_input()
		inf,sup = limits.split(' ')
		inf = int(inf)
		sup = int(sup)
		lim_inf = int(math.sqrt(inf))
		lim_sup = int(math.sqrt(sup))
		for i in range(lim_inf,lim_sup+1):
		#	print i
			if(is_palindrome(i)):
				square=i*i
				if( square>=inf ):
					if(square <= sup):
						if(is_palindrome(square)):
							cont+=1
							print i, square
					else:
						break
		print "Case #"+str(test_case+1)+": "+ str(cont)


def values():
	values = [[1, 1],
	[2, 4],
	[3, 9],
	[11, 121],
	[22, 484],
	[101, 10201],
	[111, 12321],
	[121, 14641],
	[202, 40804],
	[212, 44944],
	[1001, 1002001],
	[1111, 1234321],
	[2002, 4008004],
	[10001, 100020001],
	[10101, 102030201],
	[10201, 104060401],
	[11011, 121242121],
	[11111, 123454321],
	[11211, 125686521],
	[20002, 400080004],
	[20102, 404090404],
	[100001, 10000200001],
	[101101, 10221412201],
	[110011, 12102420121],
	[111111, 12345654321],
	[200002, 40000800004],
	[1000001, 1000002000001],
	[1001001, 1002003002001],
	[1002001, 1004006004001],
	[1010101, 1020304030201],
	[1011101, 1022325232201],
	[1012101, 1024348434201],
	[1100011, 1210024200121],
	[1101011, 1212225222121],
	[1102011, 1214428244121],
	[1110111, 1232346432321],
	[1111111, 1234567654321],
	[2000002, 4000008000004],
	[2001002, 4004009004004]]
	return values

if __name__ == "__main__":

	data = values()
	T = input()
	
	for test_case in range(T):
		cont =0
		limits = raw_input()
		inf,sup = limits.split(' ')
		inf = int(inf)
		sup = int(sup)
		#lim_inf = int(math.sqrt(inf))
		#lim_sup = int(math.sqrt(sup))
		
		for i in range(39):
			if (data[i][1] >= inf and data[i][1]<=sup):
				if(data[i][0]*data[i][0]>=inf):
					cont+=1;

		print "Case #"+str(test_case+1)+": "+ str(cont)

	
