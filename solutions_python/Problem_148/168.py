import sys
r = sys.stdin.readline

T = int(r())

for i in range(T):
    F, cap = map(int, r().split())
    sizes = list(map(int, r().split()))

    n = 0
    while sizes:
        first = sizes.pop()
        n=n+1

        for target in range(cap - first, 0, -1):
            try:
                sizes.remove(target)
                break
            except:
                pass
            pass
    result = str(n)
    print("Case #%d: %s" % (i+1, result))
