#!/usr/bin/env python
import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

def ew(s):
    ferr.write("%s\n" % s)

def ew0(s):
    pass

def get_io(argv):
    fin = sys.stdin
    fout = sys.stdout
    ifn = ofn = "-"
    if len(argv) == 2:
        bfn = sys.argv[1]
        ifn = bfn + '.in'
        ofn = bfn + '.out'
    if len(argv) > 2:
        ifn = argv[1]
        ofn = argv[2]
    if ifn != '-':
        fin = open(ifn, "r")
    if ofn != '-':
        fout = open(ofn, "w")
    return (fin, fout)

def get_numbers():
    line = fin.readline()
    return map(int, line.split())

def get_number():
    return get_numbers()[0]

def get_line():
    line = fin.readline()
    if len(line) > 0 and line[-1] == '\n':
        line = line[:-1]
    return line

def get_string():
    line = fin.readline()
    return line.strip()

def gcd(m, n):
   while n:
      t = n;
      n = m % n;
      m = t;
   return m;

def lcm(m, n):
    return (m*n)/gcd(m, n)

def lcmn(ns):
    r = ns[0]
    for n in ns[1:]:
        r = lcm(r, n)
    return r

def barberi(bs, n):
    # ew("barbers=%s, n=%d" % (bs, n))
    period = lcmn(bs)
    n_period = 0
    for b in bs:
        n_period += (period / b)
    # ew("period=%d, n_period=%d, n:=%d" % (period, n_period, n))
    n = n % n_period
    if (n == 0):
        n = n_period
    # ew("period=%d, n_period=%d, n:=%d" % (period, n_period, n))
    ba = len(bs) * [0] # baraber[] is active for next v minutes
    for c in range(n):
        k = 0
        bmin = ba[0]
        for i in range(1, len(bs)):
            if bmin > ba[i]:
                k = i
                bmin = ba[i]
        # ew("c=%d: ba=%s, k=%d, bmin=%d" % (c, ba, k, bmin))
        for i in range(len(bs)):
            ba[i] -= bmin
        ba[k] = bs[k]
    r = k + 1
    return r

if __name__ == "__main__":
    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    for ci in range(n_cases):
        n = get_numbers()[1]
        bs = get_numbers()
        r = barberi(bs, n)
        fout.write("Case #%d: %s\n" % (ci + 1, r))

    fin.close()
    fout.close()
    sys.exit(0)
