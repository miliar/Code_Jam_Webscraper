import sys
import os

output_format = 'Case #{0}: {1} {2}\n'

def task3(n,k):
	n = int(n)
	k = int(k)
	if (k==1):
		return task3_helper(n)
	if (k%2): 
		if (n%2): 
			return task3(n//2, k//2)
		return task3(n//2 - 1, k//2) # the left part is n//2 -1
	# the last one goes the the right part
	if (n%2): # 
		return task3(n//2, k//2)
	return task3(n//2, k//2)

def task3_helper(n):
	if (n%2):
		return [n//2,n//2]
	else :
		return [n//2 , n//2 - 1]

# read the input
file = open(sys.argv[1])
output = open('output.txt', 'w')
lines = file.readlines()
# the number of cases.
T = int(lines[0])
# solve the riddle and write to the output file.

for i in range(T):
	n,k = lines[i+1].split(' ')
	answer = task3(n,k)
	output.write(output_format.format(i+1,answer[0],answer[1]))