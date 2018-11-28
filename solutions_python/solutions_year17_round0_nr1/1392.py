for x in range(int(input())):
    S,K = input().split()
    S = list(S)
    K = int(K)
    flip = 0
    flag = True
    for i in range(len(S)-K+1):
        if(S[i] == "-"):
            flip += 1
            for j in range(i, i+K):
                if j <= len(S)-1:
                    if S[j] == "-":
                        S[j] = "+"
                    else:
                        S[j] = "-"
    for y in range(len(S)-1, len(S)-K, -1):
        if S[y] == "-":
            flag = False
            break
    print("Case #{0}: {1}".format(x+1, str(flip) if flag else "IMPOSSIBLE"))