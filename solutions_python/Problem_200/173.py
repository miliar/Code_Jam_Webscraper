def done(S):
    last = 0
    for x in S:
        if x < last:
            return False
        else:
            last = x
    return True

def solve(i):
    S = list(input())
    S = [int(x) for x in S]

    while not done(S):
        last = 0
        for x in range(len(S)):
            if S[x] < last:
                for y in range(x, len(S)):
                    S[y] = 9
                S[x - 1] -= 1
                break
            else:
                last = S[x]
    result = ''.join([str(x) for x in S if x > 0])
    print("Case #{}: {}".format(i, result))

t = int(input())
for i in range(t):
    solve(i+1)