T = int(input())
for n in range(T):
    S = input().strip()

    for i in range(len(S)-1, 0, -1):
        if S[i] < S[i-1]:
            S = S[:i-1] + str(int(S[i-1]) - 1) + '9'*(len(S) - i)
            
    print("Case #{}: {}".format(n+1, S.lstrip("0")))
