import os

def main():
	inputf = open("cookie-clicker-large.in", 'r')
	output = open("cookie-clicker-out-large.txt", 'w')
	tests = int(inputf.readline())
	for i in xrange(tests):
		currentTime = 0.0
		param = inputf.readline().split(" ")
		c = float(param[0])
		f = float(param[1])
		x = float(param[2])
		currRate = 2.0
		while(x/currRate > (x/(currRate + f) + c/currRate)):
			currentTime += c/currRate
			currRate += f
		currentTime += x/currRate
		output.write("Case #%d: %f\n" % (i+1, currentTime))

main()