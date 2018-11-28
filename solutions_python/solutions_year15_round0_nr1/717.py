if __name__ == "__main__":
    T = int(raw_input())
    for _ in range(T):
        s = [int(x) for x in raw_input().split()[1]]
        ans = 0
        count = 0
        for i in range(len(s)):
            if count < i and s[i] > 0:
                ans += i - count
                count = i
            count += s[i]
        print 'Case #{}: {}'.format(_ + 1, ans)
