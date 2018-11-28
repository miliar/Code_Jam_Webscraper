def solve(t):
    smax, ss = input().split()
    smax = int(smax)
    ans = 0
    accumlated = int(ss[0])
    for i in range(1, smax + 1):
        if accumlated < i:
            ans += i - accumlated
            accumlated = i
        si = int(ss[i])
        accumlated += si
    print("Case #%d: %d" % (t + 1, ans))

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        solve(t)
