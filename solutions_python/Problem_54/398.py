import fractions

file1 = open("B-large.in")
file2 = open("B-large.out", "w")
c = int(file1.readline())
print c
for i in xrange(1, c+1):
    num = file1.readline().split(" ")
    num = [int(n) for n in num]
    at = num[1]
    n = num[0]
    dif = [abs(num[a] - num[b]) for a in xrange(1,  n + 1) for b in xrange(a + 1, n + 1)]
    g = reduce(fractions.gcd, dif[1:], dif[0])
    if g == 1:
        print >>file2, ''.join(['Case #',str(i), ':']), 0
        continue
    if at % g == 0:
        print >>file2, ''.join(['Case #',str(i), ':']), 0
        continue
    print >>file2, ''.join(['Case #',str(i), ':']), g - at % g

file1.close()
file2.close()
