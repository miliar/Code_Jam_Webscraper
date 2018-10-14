fin = open('input.in','r')
fout = open('output.out','w')

lines = [line[:-1] for line in fin]

T = int(lines[0])
for cT in range(1,T + 1):
	num = [int(c) for c in lines[cT]]
	solved = False
	while not solved:
		solved = True
		partialNum = num[0]
		for i in range(1, len(num)):
			if num[i] < num[i - 1]:
				solved = False
				num = [int(c) for c in (str(partialNum - 1) + ('9' * (len(num) - i)))]
				break
			else:
				partialNum = int(str(partialNum) + str(num[i]))
	fout.write("Case #" + str(cT) + ": " + str(partialNum) + "\n")
