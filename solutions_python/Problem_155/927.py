T = int(input())
for t in range(T):
    print('Case #{}: '.format(t + 1), end='')
    counts = map(int, input().split()[1])
    ans = 0
    standing = 0
    for min_standing, count in enumerate(counts):
        if count == 0:
            continue
        if min_standing > standing:
            ans += min_standing - standing
            standing = min_standing
        standing += count
    print(ans)
