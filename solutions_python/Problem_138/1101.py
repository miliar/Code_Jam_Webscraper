def solve():
    T = int(reader.r())+1
    for t in xrange(1,T):
        case = "Case #%d: %d %d"
        N = int(reader.r())
        P1 = [float(reader.r()) for i in xrange(N)]
        P2 = [float(reader.r()) for i in xrange(N)]
        P1.sort()
        P2.sort()
        P1T = P1[:]
        P2T = P2[:]
        war = 0
        dec = 0
        for i in xrange(N):
            if P1T[-1] > P2T[-1]:
                P1T = P1T[:-1]
                P2T = P2T[1:]
                war += 1
            else:
                P1T = P1T[:-1]
                P2T = P2T[:-1]
            if P1[0] < P2[0]:
                P1 = P1[1:]
                P2 = P2[:-1]
            else:
                P1 = P1[1:]
                P2 = P2[1:]
                dec += 1
        print >>fout, case % (t, dec, war)

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
