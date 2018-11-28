from sys import argv

def flip(c):
	if c == '+':
		return '-'
	else:
		return '+'

def solve(line):
	pancakes = list(line.split(' ')[0])
	width = int(line.split(' ')[1])
	flips = 0
	for i in range(len(pancakes) - width + 1):
		if pancakes[i] == '-':
			pancakes[i:i+width] = [flip(c) for c in pancakes[i:i+width]]
			flips += 1
	
	if any(c == '-' for c in pancakes):
		return "IMPOSSIBLE"
	else:
		return str(flips)

if __name__ == "__main__":
	infile = open(argv[1], 'r')
	infile.readline()
	for (i,line) in enumerate(infile):
		print ("Case #%d: " + solve(line)) % (i+1)