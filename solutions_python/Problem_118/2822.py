from os import system
from math import sqrt
import sys
sys.stdout = open("C-small-output.txt", "w")

f = open("C-small-attempt0.in", "r")
input = f.read().strip()

input = input.split('\n')
del input[0]

def palindrome(i):
	i = str(i)
	if str(i) == i[::-1]:
		return 1
	else: return 0

for key,row in enumerate(input):
	tot = 0
	limits = row.split()
	for i in range(int(limits[0]),int(limits[1])+1):
		if palindrome(i) == 1:
			root = sqrt(i)
			if root % 1 == 0 and palindrome(int(root)) == 1:
				tot+=1
	print("Case #"+str(key+1)+": "+str(tot))

system("pause")