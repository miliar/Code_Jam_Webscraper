#!/usr/bin/python3

def flip(S, j, K):
    for i in range(j, j+K):
        if S[i] == "-":
            S = S[0:i] + "+" + S[i+1:len(S)]
        else:
            S = S[0:i] + "-" + S[i+1:len(S)]
    return S


T = int(input())

for i in range(T):
    line = str(input())

    S = line.split(" ")[0]
    K = int(line.split(" ")[1])
    number = 0

    length = len(S)
    for j in range(length):
        if S[j] == "-" and j+K <= length:
            S = flip(S, j, K)
            # print(S, j, K)
            number += 1

    if "-" in S:
        print("Case #" + str(i+1) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(i+1) + ": " + str(number))