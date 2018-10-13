t = int(raw_input())
def is_pal(n):
    n = str(n)
    return n == n[::-1]
r = []
for i in xrange(10000000):
    if is_pal(i) and is_pal(i * i):
        r.append(i * i)

for o in range(t):
    A,B = map(int,raw_input().split())
    print "Case #" + str(o+1) + ": " + str([i <= B and i >= A for i in r].count(True))
