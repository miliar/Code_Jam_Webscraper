# Magic Trick

def magic(file):
	f = open(file)
	lines = f.readlines()
	f.close()

	numtests = int(lines[0])
	rest = lines[1:]
	output = ""

	for i in range(numtests):
		num1 = rest[i*10]
		num2 = rest[i*10+5]
		row1 = rest[i*10+int(num1)].split()
		row2 = rest[i*10+int(num2)+5].split()
		# print num1
		# print row1
		# print num2
		# print row2
		inter=set(row1).intersection(row2)
		# print inter
		if len(inter)==0:
			output+="Case #"+str(i+1)+": Volunteer Cheated! \n"
		elif len(inter)==1:
			output+="Case #"+str(i+1)+": "+str(list(inter)[0]) + "\n"
		else:
			output+="Case #"+str(i+1)+": Bad magician! \n"

	return output

print magic("A-small-attempt0.in")


