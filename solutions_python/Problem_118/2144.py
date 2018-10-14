import math
def fas(i):
    rev = int(str(i)[::-1])
    sqr = math.sqrt(i)
    if int(sqr) == sqr :
        sqr = int(sqr)
        revsq = int(str(sqr)[::-1])
        if i == rev and sqr == revsq:
            return True
        return False
inf = open('foo.in', 'rU')
out = open('out.txt', 'w')
T = int(inf.readline())
for case in range(1, T+1):
    r = map(int, inf.readline().split())
    count = 0
    for x in range(r[0], r[1]+1):
        if fas(x):
            count += 1
    out.write("Case #%d: %d\n" % (case, count))
