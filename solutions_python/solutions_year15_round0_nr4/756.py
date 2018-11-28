#Shrey Gupta
#Problem D. Ominous Omino

f1 = open('D-small-attempt6.in.txt', 'r')
f2 = open('omino.out', 'w')

n = int(f1.readline().strip("\n"))

for i in range(n):
	data = f1.readline().strip("\n").split(" ")
	x = int(data[0]); r = int(data[1]); c = int(data[2])

	if x == 1:
		f2.write("Case #" + str(i+1) + ": " + "GABRIEL" + "\n")
		continue

	if x == 2:
		if (r < 2 and c < 2) or (r%2 != 0 and c%2 != 0):
			f2.write("Case #" + str(i+1) + ": " + "RICHARD" + "\n")
			continue
		else:
			f2.write("Case #" + str(i+1) + ": " + "GABRIEL" + "\n")
			continue

	if x == 3:
		if (r < 3 and c < 3):
			f2.write("Case #" + str(i+1) + ": " + "RICHARD" + "\n")
			continue
		if (r < 2 or c < 2):
			f2.write("Case #" + str(i+1) + ": " + "RICHARD" + "\n")
			continue
		if (r*c)%3 != 0:
			f2.write("Case #" + str(i+1) + ": " + "RICHARD" + "\n")
			continue			
		else:
			f2.write("Case #" + str(i+1) + ": " + "GABRIEL" + "\n")
			continue

	if x == 4:
		if (r < 4 and c < 4):
			f2.write("Case #" + str(i+1) + ": " + "RICHARD" + "\n")
			continue
		if (r < 3 or c < 3):
			f2.write("Case #" + str(i+1) + ": " + "RICHARD" + "\n")
			continue
		else:
			f2.write("Case #" + str(i+1) + ": " + "GABRIEL" + "\n")
			continue
