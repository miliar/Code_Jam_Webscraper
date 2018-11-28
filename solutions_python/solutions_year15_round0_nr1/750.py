from sys import stdin

T = int(stdin.readline())
for t in range(1, T + 1):
    S_max, S = stdin.readline().strip().split()
    S_max = int(S_max)
    S = [int(c) for c in S]
    clapping = 0
    ans = 0
    for i in range(S_max + 1):
        if clapping < i:
            ans += i - clapping
            clapping += i - clapping
        clapping += S[i]
    print("Case #%s: %s" % (t, ans))
