def solve():
    T = int(reader.r())+1
    for t in xrange(1,T):
        case = "Case #%d: " % t
        s = int(reader.r())
        x = [int(reader.r()) for i in xrange(16)]
        x = set(x[(s-1)*4:(s*4)])
        s = int(reader.r())
        y = [int(reader.r()) for i in xrange(16)]
        y = set(y[(s-1)*4:(s*4)])
        x = list(x & y)
        if len(x) == 0:
            print >>fout, case + "Volunteer cheated!"
        elif len(x) > 1:
            print >>fout, case + "Bad magician!"
        else:
            print >>fout, case + str(x[0])

class reader:
    buffer = []
    @staticmethod
    def r():
        if not reader.buffer:
            #reader.buffer = raw_input().split()
            reader.buffer = fin.readline().rstrip().split()
        temp = reader.buffer[0]
        reader.buffer = reader.buffer[1:]
        return temp
    @staticmethod
    def rl():
        return fin.readline().rstrip()
        #return raw_input()

#solve()
fin = open('test.in', 'r')
fout = open('test.out', 'w')
solve()
fin.close()
fout.close()
