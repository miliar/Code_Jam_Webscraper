#!/usr/bin/env python
import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

def ew(s):
    ferr.write("%s\n" % s)
    # pass

def gcd(m, n):
   while n:
      t = n;
      n = m % n;
      m = t;
   return m;

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



solved = {}


class Elf:
    
    def __init__(self, fin):
        pq = get_string().split('/')
        [self.p, self.q] = map(int, pq)

    def solve(self):
        d = gcd(self.p, self.q)
        twop = self.q / d
        gen = 0
        while (twop % 2) == 0:
            gen += 1
            twop /= 2
        ret = "impossible"
        if twop == 1:
            p = self.p / d
            q = self.q / d
            gen = self.rsolve(p, q)
            ret = "%d" % gen
        return ret

    def rsolve(self, p, q):
        # ew("p=%d, q=%d" % (p, q))
        d = gcd(p, q)
        p /= d
        q /= d

        g = solved.get((p, q))
        if g is None:
            if q == 1:
                g = 0 if p == 1 else 41
                # ew("g==1")
            else:
                g = 41
                for a in range(1, p + 1, 2):
                    b = p - a
                    gab = min(self.rsolve(a, q/2), self.rsolve(b, q/2)) + 1
                    if g > gab:
                        g = gab
            solved[(p, q)] = g
        return g

if __name__ == "__main__":
    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    for ci in range(n_cases):
        elf = Elf(fin)
        r = elf.solve()
        fout.write("Case #%d: %s\n" % (ci + 1, r))

    fin.close()
    fout.close()
    sys.exit(0)
