

def solve(case):
    (n,l,h) = map(int,raw_input().split())
    x = list(map(int,raw_input().split()))

    for f in range(l, h+1):
        ok = True
        for of in x:
            if of % f != 0 and f % of != 0:
                ok = False
                break
        if ok:
            print "Case #%s: %s" % (case, f)
            return
    print "Case #%s: NO" % case


def main():
    t = int(raw_input())
    for i in range(t):
        solve(i+1)

main()
