#!/usr/bin/python
import sys

def process(n, A, B, C, D, x, y, M):
	num = 0
	trees = []
	trees.append( (x , y ) )
	for i in xrange(1, n):
		x = (A * x + B) % M
		y = (C * y + D) % M
		trees.append( (x , y ) )
	#print >>sys.stdout, trees
	trees2 = []
	for (x,y) in trees:
		for (x1, y1) in trees:
			if (x,y) == (x1, y1):
				continue
			trees2.append( ( ((x+x1) % 3, (y + y1) % 3), (x,y), (x1, y1)))
	#print >>sys.stdout, trees2
	for (x,y) in trees:
		for ( (x1, y1), t1, t2) in trees2:
			if (x,y) == t1 or (x,y) == t2:
				continue
			if (x + x1) % 3 == 0 and (y + y1) % 3 == 0:
				num += 1
	return num // 6
	

def main():
    args = sys.argv[1:]
    f = args[0]
    txt = open(f).read()
    txt = txt.split("\n")
    lim = int(txt[0])
    txt = txt[1:]
    i = 0
    while i < lim:
        n, A, B, C, D, x, y, M = txt[i].split(" ")
        i += 1
        result = process(int(n), int(A), int(B), int(C), int(D), int(x), int(y), int(M))
        print "Case #%d: %s" % (i, result)

if __name__ == "__main__":
    sys.exit(main())
