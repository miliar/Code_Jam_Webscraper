def solve():
    claps = 0
    level = 0
    res = 0
    ppl = input().split()[1]
    for a in ppl:
        needed = level - claps
        if needed > 0:
            res += needed
            claps += needed
        level += 1
        claps += int(a)
    return res

t = int(input())
for i in range(0, t):
    print('Case #' + str(i+1) + ':', solve())

