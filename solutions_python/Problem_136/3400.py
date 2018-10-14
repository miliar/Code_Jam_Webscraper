# coding: utf-8

def main():

    T = int(raw_input().strip())

    for test_case in xrange(1, T + 1):

        C, F, X = map(float, raw_input().strip().split())

        res = 1000000000000.0

        for farm in xrange(10000):
            cps = [2 + F * k for k in xrange(farm + 1)]
            total = sum(C / v for v in cps[:-1]) + X / cps[-1]
            # print "farm=%d total-time=%f" % (farm, total)
            if total > res: break
            res = total

        print "Case #%d: %.8f" % (test_case, res)

if __name__ == '__main__':
    main()
