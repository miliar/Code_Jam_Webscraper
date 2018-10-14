import sys
import string

fin = file('B-large.in')
fout = file('out-large', 'w')
T = int(fin.readline())
case = 1

for line in fin:
	line = line.split(" ")
	googlers = int(line[0])
	surprising = int(line[1])
	mins = int(line[2])
	tot = 0

	for i in range(googlers):
		score = int(line[i + 3])
		vote = score / 3
		if score % 3 == 0:
			if vote >= mins:
				tot += 1
			elif surprising > 0 and vote > 0 and vote + 1 >= mins:
				surprising -= 1
				tot += 1
		elif score % 3 == 1:
			if vote >= mins or vote + 1 >= mins:
				tot += 1
			elif surprising > 0 and vote + 1 >= mins:
				surprising -= 1
				tot += 1
		elif score % 3 == 2:
			if vote >= mins or vote + 1 >= mins:
				tot += 1
			elif surprising > 0 and vote + 2 >= mins:
				surprising -= 1
				tot += 1

	fout.write("Case #" + str(case) + ": " + str(tot) + "\n")
	case += 1

