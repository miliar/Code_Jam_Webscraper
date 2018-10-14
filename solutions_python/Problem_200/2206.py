#!/usr/bin/python

from sys import *

n_cases = int(stdin.readline().rstrip("\n"),10)

for case in range(0,n_cases):
	result="0"

	number_s = stdin.readline().rstrip("\n")
	number_len = len(number_s)
	number = int(number_s,10)

	solution=True

	while(solution):
		solution = False
		if len(str(number))==1:
			break

		for i in range(0,(len(str(number))-1)):
			len_n = len(str(number))
			num_s = str(number)


			if num_s[len_n-i-2]>num_s[len_n-i-1] or num_s[len_n-i-2]=='0' or num_s[len_n-i-1]=='0':
				number = number - (10**i)
				solution = True
				break
	result=str(number)
	#print("Number",number_s,"Tidy",number)

	print("Case #"+str(case+1)+": "+result)

