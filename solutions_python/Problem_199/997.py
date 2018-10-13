# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):

	pancake_list, pancaker = input().split(" ")  # read a list of integers, 2 in this case
	
	pancaker = int(pancaker)
	
	pancake_list = list(pancake_list)
	count = 0
	for j in range(len(pancake_list)):
		if pancake_list[j] == '-' :
		
			if j+pancaker > len(pancake_list):
				count = 'IMPOSSIBLE'
				break
					
			for k in range( pancaker ):

				if pancake_list[j+k] == '-':
					pancake_list[j+k] = '+'
				else:
					pancake_list[j+k] = '-'
				
			if 	count == 'IMPOSSIBLE':
				break
				
			count += 1 
	  

	print("Case #{}: {}".format(i, count))
	# check out .format's specification for more formatting options