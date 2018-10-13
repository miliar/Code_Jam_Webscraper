

def solve():
    n, s = input().split()
    n = int(n)
    ans = 0
    sum = 0
    for i in range(len(s)):
        while sum < i:
            ans += 1
            sum += 1
        sum += ord(s[i]) - ord('0')
    print(ans)




t = int(input())
for tests in range(t):
    print('Case #', tests + 1, ': ', sep='', end='')
    solve()
