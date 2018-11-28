filename = raw_input("filename: ")
f = open(filename,"r")
g = open("D.out", "w")
num_tests = int(f.readline().rstrip())
war = []
deceit = []
for i in range(num_tests):
	num_blocks = int(f.readline().rstrip())
	naomi = f.readline().split()
	naomi = [float(e) for e in naomi]
	naomi.sort()
	ken = f.readline().split()
	ken = [float(e) for e in ken]
	ken.sort()
	current_pointer = 0
	ken_points = 0
	for i in range(num_blocks):
		if current_pointer == num_blocks:
			break
		while True:
			if current_pointer == num_blocks:
				break
			if ken[current_pointer] > naomi [i]:
				current_pointer += 1
				ken_points += 1
				break
			else:
				current_pointer += 1
	war.append(num_blocks - ken_points)
	current_pointer = 0
	naomi_points = 0
	for i in range(num_blocks):
		if current_pointer == num_blocks:
			break
		while True:
			if current_pointer == num_blocks:
				break
			if naomi[current_pointer] > ken[i]:
				current_pointer += 1
				naomi_points += 1
				break
			else:
				current_pointer += 1
	deceit.append(naomi_points)

f.close()
for i in range(num_tests):
	g.write("Case #" + str(i + 1) + ": ")
	g.write(str(deceit[i]) + " " + str(war[i]))
	if i < num_tests - 1:
		g.write("\n")
g.close()
