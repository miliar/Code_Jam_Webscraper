"""
Recycled Numbers
https://code.google.com/codejam/contest/1460488/dashboard#s=p2
"""

def main():
    T = int(raw_input())
    for id in xrange(T):
        A, B = [int(s) for s in raw_input().split()]
        strlen = len(str(A))
        ans = 0
        if strlen == 1:
            print "Case #%d: %d" % (id + 1, ans)
            continue
        for a in xrange(A, B):
            stra = str(a)
            xset = []
            for rot in xrange(1, strlen):
                x = int(stra[-rot:] + stra[:strlen-rot])
                if x not in xset and a < x and x <= B:
                    ans += 1
                    xset.append(x)
        print "Case #%d: %d" % (id + 1, ans)

main()
