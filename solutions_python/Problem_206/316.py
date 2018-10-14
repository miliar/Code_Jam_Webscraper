tc = int(input())
for v in range(tc):
    vi, vj = map(int, input().split())
    cache = []
    for _ in range(vj):
        k, s = map(int, input().split())
        cache.append((k, s))
    sorted(cache, key=lambda x: x[0])
    temp = (vi - cache[0][0]) / float(cache[0][1])
    for _ in range(1, len(cache)):
        if cache[_][1] <= cache[_ - 1][1] or (cache[_ - 1][0] - cache[_][0]) / float(cache[_][1] - cache[_ - 1][1]) > temp:
            temp = max(temp, (vi - cache[_][0]) / float(cache[_][1]))
    print("Case #%d: %.9lf" % ((v + 1), vi / float(temp)))
