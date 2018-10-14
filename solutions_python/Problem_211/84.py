import sys
from datetime import datetime


def debug(x):
    sys.stderr.write('{} DEBUG: {}\n'.format(datetime.now().time(), x))

EPS = 1e-12

def solve(N, K):
    rem = float(raw_input())
    probs = map(float, raw_input().split())
    probs.append(1.)
    while rem > EPS and (1.0-min(probs))>EPS:
        probs = sorted(probs)
        jj = 1
        for i, p in enumerate(probs[1:]):
            if p-probs[0]>EPS:
                jj = i+1
                break
        extra = min(rem, probs[jj]-probs[0])
        rem-=extra
        fra = extra/jj
        for i in xrange(jj):
            probs[i]=min(1., fra+probs[i])
    ans = 1.
    for p in probs:
        ans*=p
    return ans

def main():
    T = int(raw_input())
    for tc in xrange(1, T+1):
        debug("Running test #{}...\n".format(tc))
        N, K = map(int, raw_input().split())
        print "Case #{}: {:.8f}".format(tc, solve(N, K))


if __name__ == "__main__":
    main()
