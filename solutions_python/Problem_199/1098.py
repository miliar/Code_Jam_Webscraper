def solve():
    def flip(s, k, index):
        for i in range(k):
            s[index + i] = '+' if s[index + i] is '-' else '-'

    c = 0
    sk = input().split()
    s = list(sk[0])
    k = int(sk[1])
    for i in range(len(s) - k + 1):
        if s[i] is '-':
            flip(s, k, i)
            c += 1
    for i in range(k):
        if s[-i-1] is '-':
            return 'IMPOSSIBLE'
    return str(c)

T = int(input())
for t in range(1, T + 1):
    print('Case #%d:' % t, solve())

