def inputvars():
	f = open('A-large.in')
	num = int(f.readline())
	numlist = f.read().splitlines()
	return num, numlist

def outputvars(num, output):
	f = open('output.txt', 'w')
	for x in range(num):
		f.write('Case #' + str(x + 1) + ": " + str(output[x]))
		f.write("\n")
	f.close()

def main():
	num, numlist = inputvars()
	output = []
	for x in numlist:
		line = list(x.split()[0])
		sizeflipper = int(x.split()[1])
		numflips = 0
		for y in range(len(line)):
			# if("-" not in line):
			# 	output.append(numflips)
			# 	break
			if(line[y] == '-' and sizeflipper + y < len(line)):
				flip(line, sizeflipper, y)
				numflips += 1
			if(line[len(line) - y - 1] == '-' and (len(line) - y - sizeflipper) > -1):
				flip(line, sizeflipper, len(line) - y - sizeflipper)
				numflips += 1
		if("-" not in line):
			output.append(numflips)
		else:
			output.append("IMPOSSIBLE")
	outputvars(num, output)

def flip(line, sizeflipper, y):
	for x in range(sizeflipper):
		if(line[y + x] == '+'):
			line[y + x] = '-'
		else:
			line[y + x] = '+'

main()