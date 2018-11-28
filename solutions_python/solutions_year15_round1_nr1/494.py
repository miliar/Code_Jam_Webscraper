import math
message = open("A-large.in", 'r')
lines = message.readlines()
cases = 0
case = 0
expectingQuant = True;
Quant = 0
for line in lines:
	if case == 0:
		cases = line
		case = 1
		continue
	if expectingQuant:
		Quant = int(line)
		expectingQuant = False
		continue
	expectingQuant = True
	counts = line.split()
	if len(counts) == 1:
		print("Case #" + str(case) + ": 0 0")
		case = case + 1
		continue
	m1min = 0
	m2rate = 0
	for i in range(len(counts) - 1):
		if (int(counts[i]) - int(counts[i + 1])) > 0:
			m1min = m1min + (int(counts[i]) - int(counts[i + 1]))
		if (int(counts[i]) - int(counts[i + 1])) > m2rate:
			m2rate = (int(counts[i]) - int(counts[i + 1]))
	m2min = 0
	for i in range(len(counts) - 1):
		if int(counts[i]) > m2rate:
			m2min = m2min + m2rate
		else:
			m2min = m2min +int(counts[i])
	print("Case #" + str(case) + ": " + str(m1min) + " " + str(m2min))
	case = case + 1
