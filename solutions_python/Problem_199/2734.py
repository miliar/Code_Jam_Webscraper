T = int(input())

for i in range(1, T+1):
        (S, K) = input().split()
        K = int(K)
        if "-" not in S:
                print("Case #%d: %d" % (i, 0))
                continue
        if K > len(S):
                print("Case #%d: IMPOSSIBLE" % i)
                continue
        S = list(S)
        count = 0
        for j in range(len(S)-K+1):
                if S[j] == "+":
                        continue
                for l in range(j, j+K):
                        if S[l] == "+": S[l] = "-"
                        else: S[l] = "+"
                count += 1
                continue
        
        if "-" not in S:
                print("Case #%d: %d" % (i, count))
        else:
                print("Case #%d: IMPOSSIBLE" % i)
                
                
