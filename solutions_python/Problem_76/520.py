from operator import xor

T = input()
for i in xrange(T):
    N = input()
    C = map(int, raw_input().split())
    C.sort()
    ans = -1
    for j in xrange(1, N):
        patrick_xor = reduce(xor, C[:j])
        sean = C[j:]
        sean_xor = reduce(xor, sean)
        sean_sum = sum(sean)
        if (patrick_xor == sean_xor and sean_sum > ans):
            ans = sean_sum
    print "Case #%s: %s" % (i + 1, "NO" if ans == -1 else ans)