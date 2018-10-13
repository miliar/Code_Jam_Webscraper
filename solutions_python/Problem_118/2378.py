#!/usr/bin/python
import math

def is_Palindrome( number):
	digitList = list(str(number))
	palindrome = True
	if len(digitList) % 2 ==0:
		for i in range(0,len(digitList)/2+1):
			if digitList[i] != digitList[len(digitList) -i-1]:
				palindrome = False
				break
	else:
		for i in range(0,len(digitList)/2):
			if digitList[i] != digitList[len(digitList) -i-1]:
				palindrome = False
				break

	return palindrome

list_tuples = list()
with open("input.file","r") as f:
	num_tuples = int(f.readline())
	for i in range (0, num_tuples):
		list_tuples.append( tuple( f.readline().replace('\n','').split(" ")) )

index = 1
for i in list_tuples:
	count = 0
	low_lim = int(i[0])
	high_lim = int(i[1])
	for j in range( int(math.floor(math.sqrt(low_lim))), int(math.ceil(math.sqrt(high_lim)))+ 1):
		if is_Palindrome(j) and is_Palindrome(j*j):
			if j*j >= low_lim and j*j <= high_lim:
				count += 1
	print "Case #" + str(index)+": " + str(count)
	index += 1

