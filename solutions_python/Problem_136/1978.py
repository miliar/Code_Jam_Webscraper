import csv

def getResult(c,f,x):
    r,t = 2.0,0.0

    ts = x/r
    tb = c/r + x/(r+f)
    while ts > tb:
	t += c/r
	r += f
	ts = x/r
	tb = c/r + x/(r+f)
    t += ts
    return t

def cookieClicker(infile):
    reader = csv.reader(open(infile,'r'),delimiter=' ')
    t,t0 = int(reader.next()[0]),0
    while t0 < t:
	t0 += 1
	c,f,x = reader.next()
	c,f,x = float(c),float(f),float(x)
	rstr = getResult(c,f,x)
	print 'Case #%s: %0.7f' % (t0,float(rstr))

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('infile',metavar='infile',type=str)
    args = ap.parse_args()
    cookieClicker(args.infile)
