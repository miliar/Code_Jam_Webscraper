import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        C, F, X = map(float,sys.stdin.readline().strip().split())
        rate = 2.0
        ret = 0
        #        print C, F, X, rate, ret
        while X/rate > X/(rate+F) + C/rate:
            ret += C/rate
            rate += F
            #    print C, F, X, rate, ret
        ret += X/rate
        print "Case #{0:d}: {1:.7f}".format(t+1, ret)
