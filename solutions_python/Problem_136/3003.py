import csv

def cookies(c, f, x):
	rate = 2
	running = 0
	while x/rate > (c/rate + x/(rate+f)):
		running += c/rate
		rate += f
	running += x/rate
	return running

infile = open('B-large.in', 'r')
outfile = open('output-cookies-large.txt', 'w')
t = int(infile.readline())
for i in range(t):
	case = infile.readline().split(' ')
	answer = cookies(float(case[0]), float(case[1]), float(case[2]))
	line = "Case #" + str(i+1) + ": " + str(answer) + '\n'
	outfile.write(line)
