import sys

fn = sys.argv[1]
f = open(fn)

tline = f.readline().strip()
t = int(tline)

def generate_run_lengths(s, n):
    ss_length = 0
    for c in s:
        if c in "aeiou":
            ss_length = 0
        else:
            ss_length += 1
        yield ss_length

def nvalue(s, n):
    rl = [ c for c in generate_run_lengths(s, n) ]
    nv = 0
    per_step = 0
    for i in xrange(len(s)):
        if rl[i] >= n:
            per_step = max(0, i + 1 - (n - 1))
        nv += per_step
    return nv

for i in range(t):
    spart, npart = f.readline().strip().split()
    s = spart
    n = int(npart)
    nv = nvalue(s, n)
    print "Case #%i: %i" % (i + 1, nv)

