tc = int(input())
for i in range(1, tc + 1):
    print("Case #%d: " % i, end='')
    d, n = map(int, input().split())
    velo = 0
    h = []
    for i in range(n):
        k, s = map(int, input().split())
        h.append(float((float(d) - float(k)) / float(s)))
    velo = float(float(d) / float(max(h)))
    print("%f" % velo)
