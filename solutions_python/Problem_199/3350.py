def flip(i, j) :
    for k in range (i, j+1) :
        if S[k] == '+' :
           S[k] = '-'
        else :
            S[k] = '+'
T = int(input())
for j in range (1, T+1) :
    S = list(input().split(" "))
    k = int(S[1])
    S = list(S[0])
    temp = len(S)
    count = 0
    for i in range (0, temp - k + 1) :
        if S[i] == '-' :
            flip(i, i+k-1)
            count += 1
    result = count
    for i in range (temp - k + 1, temp) :
        if S[i] != '+' :
            result = "IMPOSSIBLE"
            break
    print("Case #", j, ": ", result, sep = "")
