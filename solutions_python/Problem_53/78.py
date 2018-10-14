import sys

fname = sys.argv[1]
f = open(fname)
tc = int(f.readline().strip())

for i in range(tc):
    l = f.readline().strip()
    n,k = l.split()
    n = int(n)
    k = int(k)
    mask = pow(2, n) - 1
    s = "OFF"
    if k & mask == mask:
        s = "ON"
    print "Case #%d: %s" % (i+1, s)
