def solve():
    n, arr = raw_input().split(" ")
    n = int(n)
    cur = 0
    ans = 0
    arr = map(int, list(arr))
    for i in range(0, n+1):
        if cur < i:
            ans += i - cur
            cur = i
        cur = cur + arr[i]
    return ans


if __name__ == "__main__":
    t = int(raw_input())
    for i in range(0, t):
        print "Case #%d: %d" % ((i+1), solve())
