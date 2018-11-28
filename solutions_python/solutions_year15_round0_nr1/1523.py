#Shrey Gupta
#Problem A. Standing Ovation

f1 = open('A-large.in.txt', 'r')
f2 = open('ovation.out', 'w')

n = int(f1.readline().strip("\n"))

for x in range(n):
	data = f1.readline().strip("\n").split(" ")
	length = int(data[0]) + 1
	string = data[1]
	num = 0
	totalPassed = 0
	for y in range(length):
		if y > totalPassed:
			num += (y - totalPassed)
			totalPassed = y
		totalPassed += int(string[y])
	out = "Case #" + str(x+1) + ": " + str(num) + "\n"
	f2.write(out)