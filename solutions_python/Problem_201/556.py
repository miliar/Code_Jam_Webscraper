
def solve():
    n, k = map(int, input().split())
    a = 1
    b = 0
    v = n


    while a + b < k:
        k -= a + b
        if v & 1:
            a, b = a * 2 + b, b
        else:
            a, b = a, b * 2 + a
        v = v // 2

    if a >= k:
        print(v // 2, (v - 1) // 2)
    else:
        print((v - 1) // 2, (v - 2) // 2)



T = int(input())
for t in range(T):
    print("Case #%d: " % (t + 1), end='')
    solve()
