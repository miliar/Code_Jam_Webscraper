from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import re, sys
#import scipy.linalg as alg
#import scipy.optimize as opt
#from pygraph.classes.digraph import digraph
#from pygraph.algorithms.minmax import maximum_flow, shortest_path, shortest_path_bellman_ford
#from pygraph.algorithms.searching import breadth_first_search, depth_first_search
#from scipy.weave import inline

def handle(infile, outfile):
	line = infile.readline().split()
	n, m = [int(x) for x in line]
	r = {}
	for i in range(n):
		line = infile.readline()[:-1].split('/')[1:]
		c = r
		for s in line:
			if not s in c:
				c[s] = {}
			c = c[s]
	z = 0
	for i in range(m):
		line = infile.readline()[:-1].split('/')[1:]
		c = r
		for s in line:
			if not s in c:
				c[s] = {}
				z += 1
			c = c[s]
	outfile.write(' %d' % z)

if len(sys.argv) != 2: exit()
infile = file(sys.argv[1] + '.in', 'r')
outfile = file(sys.argv[1] + '.out', 'w')

count = int(infile.readline())
for i in range(count):
	print 'Case #%d' % (i + 1)
	outfile.write('Case #%d:' % (i + 1))
	result = handle(infile, outfile)
	outfile.write('\n')
