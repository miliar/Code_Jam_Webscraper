import numpy as np


def unhappy(A, i, n):
	
	if(i + n > len(A)):
		i = len(A) - n
		
	flag = True
	
	for j in range(i, i+n):
		if(A[j] == "+"):
			flag = False
			break
	return flag
	
def flip(A,i,n):
	if(i + n > len(A)):
		i = len(A) - n
	
	for j in range(i, i+n):
		if(A[j] == "+"):
			A[j] = "-"
		else:
			A[j] = "+"


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	A, n = [s for s in input().split(" ")]	# read a list of integers, 1 in this case
	n = int(n)
	A = list(A)
	count = A.count("-")
	flips = 0
	if(len(A) >= n):
		for j in range(n,0,-1):
			for k in range (len(A) - j):
				if(unhappy(A, k, j)):
					flip(A,k,n)
					flips += 1
		
		for k in (A):
			if(k == '-'):
				flips = "IMPOSSIBLE"
				break
	else:
		flips="IMPOSSIBLE"
		
	print("Case #{}: {}".format(i, flips))
	# check out .format's specification for more formatting options