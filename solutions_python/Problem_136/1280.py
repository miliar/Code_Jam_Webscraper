import math

def Cookies(cost, benefit, goal):
    current = 2.0
    penalty = 0.0
    while True:
	t1 = goal/current + penalty
    	t2 = goal/(current+benefit) + penalty + cost/current
    	if t1 < t2:
            return t1
        penalty = penalty + cost/current
        current = current + benefit

def Parse():
    fin = open(r"E:\Projects\CodeJam\Cookies\B-large.in", 'r')
    fout = open(r"E:\Projects\CodeJam\Cookies\B-large.out", 'w')
    count = int(fin.readline())
    for i in range(1, count+1):
        args = [float(x) for x in fin.readline().split(" ")]
	ret = Cookies(*args)
        result = "Case #%d: %.7f\n" % (i, ret)
	fout.write(result)
    fin.close()
    fout.close()

Parse()