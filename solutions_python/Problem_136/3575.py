#t = x / 2
#t = c / 2 + x / (2 + f)
#t = c / 2 + c / (2 + f) + x / (2 + f + f)
#t = c / 2 + c / (2 + f) + c / (2 + f + f) + x / (2 + f + f + f)
import sys

def calculate(c, f, x):
	value = x / 2
	previousValue = value
	num = 1
	while value <= previousValue:
		previousValue = value
		value = x / (2 + num * f)
		for i in range(0, num):
			value += c / (2 + i * f)
		num += 1
	return previousValue

T = int(input())
for i in range(0, T):
	c, f, x = raw_input().split()
	sys.stdout.write("Case #" + str(i + 1) + ": " + str(calculate(float(c), float(f), float(x))) + "\n")