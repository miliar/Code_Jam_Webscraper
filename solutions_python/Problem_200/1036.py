# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):

	n = input().split(" ")  # read a list of integers, 2 in this case
	tidy = [int(s) for s in (list(str(n))[2:-2])][::-1]
	untidy = True
	
	while untidy:
		untidy = False
		for j in range(len(tidy)-1):
			if tidy[j] < tidy[j+1]:
				untidy = True
				for k in range(j+1):
					tidy[k] = 9
				tidy[j+1] -=1
		
	resposta = tidy[::-1]
	resp_string = ''
	
	for s in resposta:
		resp_string += str(s)

	print("Case #{}: {}".format(i, int(resp_string)))
	# check out .format's specification for more formatting options