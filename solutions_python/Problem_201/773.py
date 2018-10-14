def solve(n, k):
    nAux = n
    x = 0
    d = 1
    while x + d < k:
        nAux = (nAux - 1) // 2
        x += d
        d *= 2

    if (n - x) % d >= (k - x):
        gapSize = (n - x) // d + 1
    else:
        gapSize = (n - x) // d
    return gapSize // 2, (gapSize - 1) // 2

# print(solve(66, 33))
# exit(0)

t = int(input())
for i in range(1, t+1):
    line = input()
    n = int(line.split(" ")[0])
    k = int(line.split(" ")[1])
    (y, z) = solve(n, k)
    print("Case #{}: {} {}".format(i, y, z))