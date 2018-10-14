import sys
import bisect

def honest(N, A, B):
    A, B = A[:], B[:]
    result = 0
    for a in reversed(A):
        if a > B[-1]:
            result+= 1
            B.pop(0)
        else:
            k = bisect.bisect(B, a)
            B.pop(k)
    return result


def deceitful(N, A, B):
    A, B = A[:], B[:]
    result = 0
    for _ in xrange(N):
        if A[0] < B[0]:
            A.pop(0)
            B.pop(-1)
        else:
            result+= 1
            A.pop(0)
            B.pop(0)

    return result


def solve(N, A, B):
    A = sorted(A)
    B = sorted(B)
    return deceitful(N, A, B), honest(N, A, B)


def main():
    T = int(sys.stdin.readline())
    for k in xrange(T):
        N = int(sys.stdin.readline())
        A = map(float, sys.stdin.readline().split())
        B = map(float, sys.stdin.readline().split())
        answer = solve(N, A, B)
        print "Case #{0}: {1} {2}".format(1 + k, *answer)
        

if __name__ == '__main__':
    main()
