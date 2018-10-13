from sys import stdin


def poly(x):
    a = []
    while x > 0:
        a.append(x % 10)
        x /= 10
    b, c = a[:len(a)/2] , a[len(a)/2+(1 if len(a) % 2 else 0):]
    c.reverse()
    return b == c


#s = set()
#for i in xrange(100000000000):
#    if poly(i) and poly(i*i):
#        s.add(i*i)
#        print i, i*i

s = set()
def add(x):
    x = int(x)
    if poly(x * x):
        s.add(x * x)

add(1)
add(2)
add(3)

for i in xrange(2,20):
    for j in xrange(2 ** (i/2 - 1), 2 ** (i/2)):
        x = j
        a = ""
        while x > 0:
            a += str(x % 2)
            x /= 2
        if i % 2:
            add(a[::-1] + "0" + a)
            add(a[::-1] + "1" + a)
        else:
            add(a[::-1] + a)
    a = "2" + "0" * (i-2) + "2"
    add(a)
    if i % 2:
        a = a[:i/2] + "1" + a[i/2 + 1:]
        add(a)


n = int(stdin.readline())
for tc in xrange(1, n + 1):
    a, b = (int(x) for x in stdin.readline().split())
    print "Case #{0}:".format(tc),
    ans = 0
    for x in s:
        if a <= x <= b:
            ans += 1
    print ans

