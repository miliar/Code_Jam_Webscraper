def solve():
    T = int(reader.r())+1
    for t in xrange(1,T):
        case = "Case #%d: %.7f"
        C,F,X = (float(reader.r()) for i in xrange(3))
        ans = 0
        r = 2
        while True:
            c = C / r
            c2 = X / (r+F) + c
            x = X / r
            if c2 < x:
                r += F
                ans += c
            else:
                ans += x
                break;
        print >>fout, case % (t, ans)

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
