# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

#print("How many test cases?\n")
t = int(input())  # read a line with a single integer

#function to check if n is a tidy number
def isTidy(n):
	list = [int(e) for e in str(n)]
	for i in range(len(list)-1):
		if list[i+1] < list[i]:
			#print("digit["+str(i+1)+"] caused it not-tidy")
			return False, i+1
	return True, None


#function to return the highest tidy number less than/equal to n
def highestTidy(n):
	logic, index = isTidy(n)
	if not logic:
		n = str(n)
		runOfNine = len(n)-index
		#replacement = int(n[:index-1] + n[index] + runOfNine*'9')
		replacement = int(n[:index-1] + str(int(n[index-1])-1) + runOfNine*'9')
		#print("replacement = " + str(replacement))
		return highestTidy(replacement)
	else:
		#print(n)
		return n


for i in range(1, t + 1):
	#print("Type test_case["+str(i)+"] in the following format: a\n")
	n = int(input())
	highest = highestTidy(n)
	print("Case #{}: {}".format(i, highest))