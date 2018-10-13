import sys
def process(n, s, p, best):
    y = 0
    for b in best:
        if b == 0:
            if p <= 0:
                y += 1
        elif b == 30:
            if p <= 10:
                y += 1
        elif b == 29:
            if p <= 10:
                y += 1
        else:
            rem = b % 3
            quo = b / 3
            if rem == 0:
                if quo >= p:
                    y += 1
                elif quo == p - 1 and s > 0:
                    y += 1
                    s -= 1
            elif rem == 1:
                if quo + 1 >= p:
                    y += 1
            elif rem == 2:
                if quo + 1 >= p:
                    y += 1
                elif quo + 1 == p - 1 and s > 0:
                    y += 1
                    s -= 1
    return y

n = int(sys.stdin.readline())
for i in xrange(1, n+1):
    line = sys.stdin.readline()
    ints = [int(j) for j in line.split()]
    y = process(ints[0], ints[1], ints[2], ints[3:])
    print "Case #"+str(i)+": "+str(y)
