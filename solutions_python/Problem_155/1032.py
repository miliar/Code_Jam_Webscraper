def w(o):
    print >>fout, o

def solve():
    T = int(reader.r()) + 1
    for t in xrange(1, T):
        n = int(reader.r())
        s = reader.r()
        count = 0
        a = 0
        i = 0
        for x in s:
            y = int(x)
            z = 0
            if count < i:
                z = i - count
            count += z + y
            a += z
            i += 1
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

