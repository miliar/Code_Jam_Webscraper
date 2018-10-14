n =  int(input())
out = open("c:/ws/codejam/b.out", "w")

for j in range(n):
    d = int(input())
    arr = [int(j) for j in input().split(" ")]
    lim = max(arr)

    best = lim
    for w in range(1, lim - 1):
        current = 0
        tmp = arr[:]
        t = max(tmp)
        while t > w:
            tmp.remove(t)
            tmp += [t - w, w]
            t = max(tmp)
            current += 1
        best = min(best, current + t)
    out.write("Case #%d: %d" % (j + 1, best) + "\n")
out.close()