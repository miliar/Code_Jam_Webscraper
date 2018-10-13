import bisect

def w(o):
    print >>fout, o

def solve():
    T = int(reader.r()) + 1
    for t in xrange(1, T):
        X = int(reader.r())
        R = int(reader.r())
        C = int(reader.r())
        a = "RICHARD"
        if X == 1:
            a = "GABRIEL"
        elif X == 2 and (R*C) % 2 == 0:
            a = "GABRIEL"
        elif X == 3 and (R == 3 or C == 3) and R <> 1 and C <> 1:
            a = "GABRIEL"
        elif X == 4 and (R*C) >= 12:
            a = "GABRIEL"
        w("Case #%d: %s" % (t,a))

class reader:
    buffer = []
    @staticmethod
    def r():
        if not reader.buffer:
            reader.buffer = fin.readline().split()
        temp = reader.buffer[0]
        reader.buffer = reader.buffer[1:]
        return temp
    @staticmethod
    def rl():
        return fin.readline()

fin = open('test.in', 'r')
fout = open('test.out', 'w')
solve();
fin.close()
fout.close()

