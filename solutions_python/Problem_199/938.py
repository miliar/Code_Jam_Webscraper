#!/usr/bin/pypy3
pr = lambda n, m: print("Case #{}: {}".format(n,m))
IMP="IMPOSSIBLE"
UP="+"
DOWN="-"
def flip(stack, start, end):
    num = stack[:start] \
        + ''.join(['-' if x == '+' else '+' for x in stack[start:end]]) \
        + stack[end:]
    return num
N=int(input())
for I in range(N):
    inp = input().split(" ")
    stack = inp[0]
    K = int(inp[1])
    bl = "-"*K
    ml = "+"*K
    fin = "+"*len(stack)
    fl = 0
    for i in range(len(stack))[:len(stack)-K+1]:
        flg=False
        if stack[i:i+K] == ml: 
            continue
        if stack[i:i+K] == bl:
            stack = flip(stack, i, i+K)
            fl += 1
            continue
        trial = flip(stack, i, i+K)
        for k in range(K):
            if trial[i+k:i+k+K] == bl:
                stack = trial
                fl += 1
                flg = True
                break
        if not flg and stack[i] == "-":
            fl += 1
            stack = flip(stack, i, i+K)
    if stack != fin:
        print("Case #{}: IMPOSSIBLE".format(I+1))
    else:
        print("Case #{}: {}".format(I+1, fl))

