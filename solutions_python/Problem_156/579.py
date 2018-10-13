if __name__ == "__main__":
    T = int(raw_input())
    for _ in range(T):
        raw_input()
        p = map(int, raw_input().split())
        ans = max(p)
        for i in range(1, max(p)):
            count = 0
            for j in range(len(p)):
                count += (p[j] - 1) / i
            count += i
            ans = min(ans, count)
        print 'Case #{}: {}'.format(_ + 1, ans)
