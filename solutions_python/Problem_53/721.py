import sys

def parse(f):
        for line in f:
                yield line.rstrip('\n').split(" ")

def process(a, n, k):
	if ((k+1)%(2**n)):
		res = "OFF"
	else:
		res = "ON"
	print ("Case #%i: %s") % (a, res)

f = open(sys.argv[1])
f.readline()
a = 1
for lst in parse(f):
	process(a, int(lst[0]), int(lst[1]))
	a += 1
