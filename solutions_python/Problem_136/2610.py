import sys


def calculate(C, F, X, ratio):
    collect = X/ratio
    buyfarm = C/ratio + X/(ratio +F)

    return (collect - buyfarm)


file = open(sys.argv[1], "r")

num_cases = int(file.readline())

for j in xrange(1, num_cases+1):
    line = file.readline()
    info = line.split()
    C = float(info[0])
    F = float(info[1])
    X = float(info[2])
    totaltime = 0.0
    ratio = 2.0

    while(True):
	diff = calculate(C, F, X, ratio)
	if diff <= 0:
	    totaltime += X/ratio
	    break
	if diff > 0:
	    totaltime += C/ratio
	    ratio += F
	
    print "Case #%d: %.7f" %(j, totaltime)
