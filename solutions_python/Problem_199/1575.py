from sys import stdin, stdout

def swap_symbol(sym):
    return "+" if sym == "-" else "-"

def solve(S, width):
    S = list(S)
    swaps = 0
    for i, s in enumerate(S):
        if i <= (len(S) - width) and s != "+":
            swaps += 1
            S[i:i+width] = map(swap_symbol, S[i:i+width])
        elif s != "+":
            return "IMPOSSIBLE"

    return swaps


T = int(stdin.readline())

for t in range(T):
    S, width = stdin.readline().strip().split()
    width = int(width)

    result = solve(S, width)

    stdout.write("Case #%d: %s\n"%(t+1, result))