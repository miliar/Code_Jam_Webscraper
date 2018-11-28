import sys

def readint(): return int(raw_input())
def readlong(): return long(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, reader):
	res = []
	for i in range(N):
		res.append(reader())
	return res
def readlinearray(typecast): return map(typecast, raw_input().split())



def redirectio():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        infile = filename + ".in"
        outfile = filename + ".out"
        print "Opening %s..." % filename
        sys.stdin = open(infile)
        sys.stdout = open(outfile, 'w')

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

def apocalipsetime(t):
    t.sort()
    dt = [t[i]-t[i-1] for i in range(1, len(t))]
    while 0 in dt:
        dt.remove(0)
    divisor = dt[0]
    for i in range(1, len(dt)):
        divisor = gcd(dt[i], divisor)
    return (divisor - t[0]) % divisor
    

redirectio()
C = readint()
for c in range(C):
    Nt = readlinearray(long)
    t = Nt[1:]
    res = apocalipsetime(t)
    print "Case #%d: %d" % (c + 1, res)

    
    
    
    
    
    
