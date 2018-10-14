import bisect

def w(o):
    print >>fout, o

def solve():
    T = int(reader.rl()) + 1
    for t in xrange(1, T):
        D = int(reader.rl())
        s = [int(x) for x in reader.rl().split()]
        s.sort()
        c = True
        a = 0
        while c:
            count = 1
            i = -2
            temp = s[-1]
            if temp <= 3:
                a += temp
                break
            while -i <= len(s) and s[i] == temp:
                count += 1
                i -= 1
            temp = s[-1] / 2
            if count < temp and (-i > len(s) or s[-1] - s[i] > count):
                if count == 1 and s[-1] == 9 and (-i > len(s) or (-i <= len(s) and (s[i] == 1 or s[i] == 2 or s[i] == 3 or s[i] == 6))):
                    temp = 6
                a += count
                temp2 = s[-1] - temp;
                for j in xrange(count):
                    del s[-1]
                for j in xrange(count):
                    bisect.insort(s, temp2)
                    bisect.insort(s, temp)
            elif count < temp and -i <= len(s) and  s[-1] - s[i] <= count:
                y = s[i]
                while -i <= len(s) and s[-1] - s[i] <= count:
                    count += 1
                    if count >= temp:
                        c = False
                        break
                    i -= 1
                if not c:
                    a += s[-1]
                    break
                a += count
                if count == 1 and s[-1] == 9 and (-i > len(s) or (-i <= len(s) and (s[i] == 1 or s[i] == 2 or s[i] == 3 or s[i] == 6))):
                    temp = 6
                temp2 = s[-1] - temp
                for j in xrange(count):
                    del s[-1]
                for j in xrange(count):
                    bisect.insort(s, temp2)
                    bisect.insort(s, temp)
            else:
                a += s[-1]
                c = False
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

