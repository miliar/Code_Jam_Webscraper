
inp = open("B-small-attempt0.in", "r")
out = open("output.txt", "w+")


t = inp.readline()

for case in range(int(t)):
	n = inp.readline().strip('\n')
	if int(n) > 1000:
		break
	print n
	swap = 0
	tr = True
	while True:
		for i, num in enumerate(n):
			if i > 0:
				if swap > int(num):
					tr = False
					break
				else:
					tr = True
			swap = int(num)
			
		if len(n) == 1 or tr:
			break
		else:
			n = str(int(n)-1)
	out.write('Case #' + str(case+1) + ": " + n + '\n')
