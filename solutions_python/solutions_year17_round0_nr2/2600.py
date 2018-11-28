##  Code written by: Thi Hong Ngoc Do
##  D/O/B: 06/12/1989
##  Email: dothngoc@gmail.com
##  Address: 64 Atheldene Drive, St Albans, VIC 3021, Australia
##  Phone number: +61 401 418 065
##
##  Google Code Jam 2017 - Qualification Round

def find_last_tidy(n):
	if n < 10:
		return n
	elif n == 10:
		return 9

	str_n = str(n)

	new = []
	for i in range(len(str_n)):
		new.append(str_n[i])

	# Look for position where the next digit is smaller than the one before
	i=0
	smaller = True
	while smaller == True:
	#while i < (len(str_n)-1):
		if i < len(str_n)-1:
			if str_n[i] <= str_n[i+1]:
				i+=1
			else:
				break
		else:
			break

	# Found digit (index = i)
	if i == len(str_n)-1:
		return n
	else:
		for j in range(i+1,len(new)):
			new[j] = '0'

		while (i >= 0) and (new[i] <= new[i-1]):
			new[i] = '0'
			if (i>0):
				i -= 1

		result = ''.join(new)

		return (int(result))-1


############
# main #

in_file = open("B-large.in.txt", "r")
out_file = open("B_output_large.txt", "w+")

case_count = int(in_file.readline().strip())

j = 0
while j < case_count:
	n = int(in_file.readline().strip())

	result = find_last_tidy(n)

	out_file.write("Case #" + str(j+1) + ": ")
	out_file.write(str(result)+'\n')

	j += 1




in_file.close()
out_file.close()
