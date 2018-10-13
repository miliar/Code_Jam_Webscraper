from math import floor

def solution(n):
	count = 0
	while (len(n) > 0):
	    	
	    if is_tidy(n):
	     	return str(int(n + count * "9"))
	    
	    count += 1
	    n = n[:-1]
	    n = str(int(n) - 1)
	return 1


def is_tidy(n):
	current_limit = 9
	while len(n) > 0:
		right_digit = int(n[-1])
		if right_digit > current_limit:
			return False
		n = n[:-1]
		current_limit = right_digit
	return True



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(input())  # read a line with a single integer
for i in range(1, total + 1):
  n= input().strip()  # read as string, kill excess spaces
  result = solution(n)
  print("Case #{}: {}".format(i, result))
  # check out .format's specificatin for more formatting options