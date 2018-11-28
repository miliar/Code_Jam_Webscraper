T = int(input())
for tc in range(T):
    C,F,X = map(float,input().split())
    s, n, last = 0, 0, float('inf')
    while 1:
        f = s + X/(2+F*n)
        if f > last:
            print("Case #%d: %.20f" % (tc+1, last))
            break
        s += C/(2+F*n)
        n += 1
        last = f

