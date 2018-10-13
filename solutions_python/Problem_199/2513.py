def sol(s, k):
    ans = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            ans += 1
            ts = ''

            for j in range(i,i+k):
                ts += '+' if s[j] == '-' else '-'
            s = s[:i] + ts + s[i+k:]

    return ans if s.count('-') == 0 else 'IMPOSSIBLE'

t = int(input())
for i in range(t):
    s, k  = input().split()

    print('Case #%d: %s' % (i+1, sol(s, int(k))))
