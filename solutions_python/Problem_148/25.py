def solve(testNum):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    used = [False] * n
    res = 0
    pos = n - 1
    lpos = 0
    while pos >= lpos:
        if pos != lpos:
            if A[pos] + A[lpos] <= x:
                lpos += 1
        res += 1
        pos -= 1
    
    print("Case #{}: {}".format(testNum, res))

    
t = int(input())
for i in range(t):
    solve(i + 1)
