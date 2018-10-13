from time import sleep

def check(lawn):
	case = 1 #1 = good, 2 = bad

	for i in range(len(lawn)):
		for j in range(len(lawn[i])):
			num = lawn[i][j]
			count = 0
			for k in range(len(lawn)):
				if lawn[k][j] > num:
					count += 1
					break
			for k in range(len(lawn[i])):
				if lawn[i][k] > num:
					count += 1
					break

			if count == 2:
				case = 2
				break
	return case

file = open('input.txt')
cases = int(file.readline().strip())

lawns = []
for i in range(0, cases):
	lawns.append([])
	line = file.readline().strip()
	split = line.split()
	rows = int(split[0])
	cols = int(split[1])

	for j in range(0, rows):
		lawns[i].append([])
		line = file.readline().strip()
		split = line.split()

		for k in range(0, cols):
			lawns[i][j].append(int(split[k]))

f = open('output.txt', 'w')
i = 0
for lawn in lawns:
	i += 1
	state = check(lawn)
	
	if state == 1:
		f.write("Case #"+str(i)+": YES\n")
	elif state == 2:
		f.write("Case #"+str(i)+": NO\n")