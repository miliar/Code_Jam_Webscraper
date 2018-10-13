import sys
def process(case,c,f,x) :
	global mini
	result = 0
	ck = 2.0
	mini = x/ck
	if ck < x:
		while True:
			result += c/ck
			if result+x/(ck+f) < mini or mini == -1:
				mini = result+x/(ck+f)
				ck += f
			else:
				break
	else:
		mini = x/ck
	print "Case #%d: %.7f" % (case, mini)

fs = open(sys.argv[1])
n = int(fs.readline())
for i in range(n) :
	data = fs.readline().split()
	c = float(data[0])
	f = float(data[1])
	x = float(data[2])
	process(i+1,c,f,x)
