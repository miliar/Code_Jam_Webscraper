import math
import bisect


def CASE(IN):
    def rstr():
        return IN.readline().strip()

    def rint():
        return int(rstr())

    def rints():
        return map(int, rstr().split())
    N, C = rints()
    A = rints()
    A.sort()
    A = [[a, i, False] for i, a in enumerate(A)]
    r = 0
    for a, i, u in reversed(A):
        if u:
            continue
        b = C - a
        r += 1
        j = i
        A[i][2] = True
        # print "%2i: %i (%i)" % (r, a, b)
        if b > 0:
            jnew = bisect.bisect_right(A, [b, i, False], lo=0, hi=j)
            # print j, b, A[:j], jnew
            j = jnew - 1
            while j >= 0 and A[j][2] is True:
                j -= 1
            if j >= 0:
                A[j][2] = True
                # print "%2i: %i" % (r, A[j][0])
    return r


def RUN(IN, OUT):
    t = int(IN.readline().strip())
    for i in xrange(1, t + 1):
        OUT.write("Case #%i: %s\n" % (i, CASE(IN)))

if __name__ == "__main__":
    import sys
    RUN(sys.stdin, sys.stdout)
