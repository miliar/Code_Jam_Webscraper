def solve(n, k):
    if n == k:
        return 0, 0
    minimun = maximun = 0
    prev_minimun = []
    for _ in range(k):
        if n % 2 == 1:
            minimun = maximun = int(n / 2)
        else:
            minimun = int(n / 2) - 1
            maximun = int(n / 2)
        if prev_minimun and max(prev_minimun) > maximun:
            n = max(prev_minimun)
            prev_minimun.remove(max(prev_minimun))
            prev_minimun.append(maximun)
        else:
            n = maximun
        prev_minimun.append(minimun)
    return maximun, minimun


t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    maximun, minimun = solve(n, k)
    print("Case #{}: {} {}".format(i, maximun, minimun))
