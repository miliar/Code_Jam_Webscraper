from pylab import *
import sys

f = open(sys.argv[1],'r');
g = open(sys.argv[2],'w');
n = int(f.readline().strip());
for i in xrange(n):
	j1 = int(f.readline().strip())-1;
	for j in xrange(4):
		l = f.readline();
		if j == j1: r1 = np.fromstring(l.strip(),dtype=int,sep=" ");
	j2 = int(f.readline().strip())-1;
	for j in xrange(4):
		l = f.readline();
		if j == j2: r2 = np.fromstring(l.strip(),dtype=int,sep=" ");
	k = np.intersect1d(r1,r2); kl = len(k);
	if kl > 1:
		g.write("Case #%d: Bad magician!\n"%(i+1));
	if kl == 1:
		g.write("Case #%d: %d\n"%(i+1,k[0]));
	if kl == 0:
		g.write("Case #%d: Volunteer cheated!\n"%(i+1));
