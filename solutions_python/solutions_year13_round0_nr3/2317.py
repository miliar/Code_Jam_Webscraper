import sys
import urllib2

f = urllib2.urlopen("http://oeis.org/A057136/b057136.txt")
lines = [l for l in f]
p = [int(line.split()[1]) for line in lines[1:]]
f = open(sys.argv[1])
TC = int(f.readline())

for tc in xrange(TC):

    A, B = f.readline().split()
    print "Case #%d: %d" % (tc + 1, len([i for i in p if int(A) <= i <= int(B)]))
