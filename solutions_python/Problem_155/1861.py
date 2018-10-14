message = open("A-large.in", 'r')
lines = message.readlines()
cases = 0
case = 0
for line in lines:
	if case == 0:
		cases = line
		case = 1
		continue
	total = 0
	needed = 0
	position = 0
	items = line.split()
	for num in items[1]:
		if total < position:
			needed = needed + (position - total)
			total = position
		total = total + int(num)
		position = position + 1
	print("Case #" + str(case) + ": " + str(needed))
	case = case + 1
