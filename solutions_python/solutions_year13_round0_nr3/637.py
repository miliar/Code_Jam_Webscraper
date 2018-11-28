def test(val):
    s = str(val)
    if s != s[::-1]:
        return False
    s = str(val ** 2)
    if s != s[::-1]:
        return False
    return True

L = []
for i in xrange(0, 10**7+10):
    if (test(i)):
        L.append(i*i)

def count(a, b):
    cnt = 0
    for val in L:
        if val >= a and val <= b:
            cnt += 1
    return cnt

z = int(raw_input())
for i in range(z):
    a, b = map(int, raw_input().strip().split())
    print ("Case #%d: %d" % (i+1, count(a, b)))
