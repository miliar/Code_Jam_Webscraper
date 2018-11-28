def solve():
    inp = input().split(" ")
    s = list(map(lambda c : c == '-', inp[0]))
    k = int(inp[1])
    flips = 0
    for i in range(len(s)):
        if s[i]:
            for j in range(k):
                if i + j >= len(s):
                    return "IMPOSSIBLE"
                s[i + j] ^= True
            flips += 1

    return str(flips)

for i in range(int(input())):
    print(f"Case #{i+1}: {solve()}")
