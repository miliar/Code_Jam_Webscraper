
infile = open("input.txt", "r")
outfile = open("output.txt", "w")
num_cases = int(infile.readline())

cases = []
max_shyness = []
int_max_shyness = []
people = []

for i in range(0, num_cases):
	cases.append(infile.readline())
	temp1, temp2 = cases[i].split()
	max_shyness.append(temp1)
	people.append(temp2)
	int_max_shyness.append(int(max_shyness[i]))

for j in range(0,len(people)):
	people_standing = 0
	friends_to_invite = 0
	for k in range(0, int_max_shyness[j]+1):
		if k <= people_standing:
			people_standing += int(people[j][k])
		elif int(people[j][k]) != 0:
			friends_to_invite += (k - people_standing)
			people_standing += (int(people[j][k]) + friends_to_invite)
	writeline = "Case #" + str(j+1) + ": " + str(friends_to_invite) + "\n"
	outfile.write(writeline)

infile.close()
outfile.close()







