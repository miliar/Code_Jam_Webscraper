##  Code written by: Thi Hong Ngoc Do
##  D/O/B: 06/12/1989
##  Email: dothngoc@gmail.com
##  Address: 64 Atheldene Drive, St Albans, VIC 3021, Australia
##  Phone number: +61 401 418 065
##
##  Google Code Jam 2017 - Qualification Round

def calculate(s,k):
	if s == '+'*len(s):
		return str(0)+'\n'

	new = []
	for i in range(len(s)):
		new.append(s[i])
	#print(new)

	i = 0
	count = 0
	while i <= len(s)-k:
		if '-' in new:
			i = new.index('-')
			#print("i position: %d" %i)
			if i > len(s)-k:
				break
		else:
			break

		#print("count: " + str(count))
		for j in range(i,i+k):
			if new[j]=='+':
				new[j] = '-'
			else:
				new[j] = '+'
		count+=1
		#print("count: %d" %count)

	if new == ['+']*len(s):
		return str(count)+'\n'
	else:
		return "IMPOSSIBLE\n"


############
# main #

in_file = open("A-large.in.txt", "r")
out_file = open("A_output_large.txt", "w+")

case_count = int(in_file.readline().strip())

j = 0
while j < case_count:
	str_line = in_file.readline().strip()

	str_list = str_line.split()
	#print(str_list)

	s = str_list[0]
	k = int(str_list[1])

	result = calculate(s,k)

	out_file.write("Case #" + str(j+1) + ": ")
	out_file.write(result)

	j += 1

in_file.close()
out_file.close()
