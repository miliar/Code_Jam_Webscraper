import sys

def gcd(a,b):
    if b==0: return a
    return gcd(b,a-b*(a/b))

fin = open(sys.argv[1],'rU')
fout = open(sys.argv[2],'w')
C = int(fin.readline().strip())

for case,line in enumerate(fin):
    inputs = map(int,line.split())
    N, xs = inputs[0], inputs[1:]
    diffs = [abs(xs[i]-xs[i+1]) for i in xrange(N-1)]
    gcd_diffs = reduce(gcd,diffs)
    next_time = xs[0]%gcd_diffs
    if next_time == 0:
        y = 0
    else:
        y = gcd_diffs-(xs[0]%gcd_diffs)
    fout.write("Case #%i: %s\n" % (case+1, y))

fin.close()
fout.close()