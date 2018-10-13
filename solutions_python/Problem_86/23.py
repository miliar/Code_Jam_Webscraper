# Google Code Jam : Round 1C 2011 : Problem C. Perfect Harmony
# https://code.google.com/codejam/contest/dashboard?c=1128486#s=p2
# Python 2.6.5

def solve_case(t, L, H, notes):

    for i in xrange(L, H + 1):
        good = True
        for n in notes:
            if n > i and n % i != 0:
                good = False
                break
            if i > n and i % n != 0:
                good = False
                break

        if good:
            print "Case #" + str(t) + ": " + str(i)
            return

    print "Case #" + str(t) + ": NO"


def solve():
    T = int(raw_input())
    for t in range(1, T + 1):
        s = raw_input().split()
        N = int(s[0])
        L = int(s[1])
        H = int(s[2])

        s = raw_input().split()
        notes = [int(i) for i in s]

        solve_case(t, L, H, notes)

solve()
