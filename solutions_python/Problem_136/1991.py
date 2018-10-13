from pylab import *;
import sys;

f = open(sys.argv[1],'r');
g = open(sys.argv[2],'w');
n = int(f.readline().strip());
for i in xrange(n):
	C, F, X = np.fromstring(f.readline().strip(),dtype=float64,sep=" ");
	nf = int(ceil((X/C)-(2/F)-1.)); 
	if nf < 0: nf = 0;
	t = 0;
	for j in xrange(nf):
		t = t + C/(2. + j*F);
	t = t + X/(2. + nf*F);
	g.write("Case #%d: %.7lf\n"%(i+1,t));
