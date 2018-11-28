def problem2 (num):
	if len(num) == 1:
		return num


	while True:

		lst = list(num)
		
		lst2 = list(lst)

		#print (lst, lst2)
		#print (lst.sort(), lst2)
		lst.sort()
		if lst == lst2:
			return ''.join(lst2)
		else:
			num = str(int(''.join(lst2)) - 1) 



import re
f_out = open('A_output_large.txt', 'w')
f_in = open('B-small-attempt1.in', 'r')
#print f_in.readlines()
lines = [line.strip() for line in f_in.readlines()][1:]
#print (lines)

#test_case=[]
#one_case=[]
for idx in range(len(lines)):

	ans = problem2(lines[idx])

	# writes an answer (in a new line) to the output file
	f_out.write("Case #{0}: {1}\n".format(idx+1, ans))

f_out.close()

