T = int(input())
for tc in range(1, T+1):
    S_max, S = input().split()
    S_max = int(S_max)
    S = [ord(ch)-ord('0') for ch in S]
    ans = 0
    tot = 0
    for s in range(S_max+1):
        if tot < s:
            ans += s-tot
            tot = s
        tot += S[s]
    print("Case #{}: {}".format(tc, ans))
