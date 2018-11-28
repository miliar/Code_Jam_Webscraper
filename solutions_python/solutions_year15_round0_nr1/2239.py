n = int(input())
S = [list(input().split(' ')) for _ in range(n)]

for j, s in enumerate(S):
    c, f = 0, 0
    for i, m in enumerate(s[1]):
        if c < i:
            f += i - c
            c += int(m) + i - c
        else:
            c += int(m)
    print('Case #{0}: {1}'.format(j+1, f)) 


