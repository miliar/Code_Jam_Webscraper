import sys

def main(input):
    T = int(input.readline())

    for i in range(T):
        print "Case #%s:"% (i+1),

        A, B, K = map(int, input.readline().split())

        count = 0
        for a in xrange(A):
            for b in xrange(B):
                if a & b < K:
                    count += 1

        print count

main(sys.stdin)
