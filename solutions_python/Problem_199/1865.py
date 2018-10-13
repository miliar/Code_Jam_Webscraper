

f = open("Oversized Pancake Flipper.txt", "w")
T = int(input())
for i in range(T):
    print(i)
    S,K = input().split()
    K = int(K)
    n = 0
    for j in range(len(S)-K+1):
        if S[j] == '-':
            n += 1
            for k in range(K):
                if S[j+k] == '-':
                    S = S[:j+k]+'+'+S[j+k+1:]
                else:
                    S = S[:j+k]+'-'+S[j+k+1:]
    
    f.write("Case #%d: "%(i+1))
    if S.count('-') > 0:
        f.write("IMPOSSIBLE\n")
    else:
        f.write("%d\n"%n)
f.close()
