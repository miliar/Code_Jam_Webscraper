#!/usr/bin/env python3

def flip(seq, s, e):
    for i in range(s, e):
        if seq[i] == "-":
            seq[i] = "+"
        else:
            seq[i] = "-"

def _solve(i, S, K):
    n = 0
    S = list(S)
    for j in range(len(S)-K+1):
        if S[j] == "-":
            flip(S, j, j+K)
            n += 1

    res = n if all(s == "+" for s in S) else "IMPOSSIBLE"
    return res

def solve(i, S, K):
    a = _solve(i, S, K)
    b = _solve(i, S[::-1], K)
    if a == "IMPOSSIBLE":
        res = b
    elif b == "IMPOSSIBLE":
        res = a
    else:
        res = min(a, b)
    print("Case #{}: {}".format(i, res))

def main():
    t = int(input())
    for i in range(1, t+1):
        S, K = input().split(" ")
        S, K = str(S), int(K)
        solve(i, S, K)

if __name__ == "__main__":
    main()
