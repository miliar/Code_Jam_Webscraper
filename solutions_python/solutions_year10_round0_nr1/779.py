def calc(N, K):
        for i in xrange(N):
                if K % 2 == 0: return False
                K = K // 2
        return True

T = input()
for i in xrange(T):
        N, K = [int(n) for n in raw_input().split()]
	print "Case #%i: %s" % (i+1, "ON" if calc(N, K) else "OFF")

