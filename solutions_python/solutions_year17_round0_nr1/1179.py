def solve(s,k):
    l = len(s)
    n_pos = s.count('+')
    n_neg = s.count('-')

    i = 0
    flips = 0
    while i <= l-k:
        if s[i] == '-':
            flips += 1
            for j in range(i,i+k):
                s[j] = '+' if s[j]=='-' else '-'

        i += 1
    return "%d" % flips if s.count('+') == l else "IMPOSSIBLE"
_T = int(input())

for _i in range(1, _T + 1):

    line = input().split(" ")
    s = list(line[0])
    k = int(line[1])

    print("Case #%d: %s" % (_i, solve(s,k)))
