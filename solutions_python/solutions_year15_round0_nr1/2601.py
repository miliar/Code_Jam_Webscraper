
def solve(Smax, S):
    extra = 0
    for i, j in enumerate(S):
        if i == 0:
            continue
        while i > sum(S[:i]) + extra:
            extra += 1
    return extra

T = int(input())
for t in range(T):
    line = input().strip().split(" ")
    Smax = line[0]
    S = [int(x) for x in line[1]]

    print("Case #{}: {}".format(t + 1, solve(Smax, S)))