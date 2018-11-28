T = input()
def check(num, k):
    for a in num[:k]:
        if a > num[k]:
            return False
    return True

for test in xrange(T):
    n = map(int, raw_input().strip())
    for x in xrange(len(n)-1, -1, -1):
        while not check(n, x):
            n[x] -= 1
            if n[x] < 0:
                for i in xrange(x, len(n)):
                    n[i] = 9
                n[x-1] -= 1
    while n[0] == 0:
        n = n[1:]
    print "Case #%d: %s" % (test+1, ''.join(map(str, n)))
