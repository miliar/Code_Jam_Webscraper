def solve(n, p, g):
    mod = [0] * 5
    for x in g:
        mod[x % p] += 1
    if p == 2:
        result = mod[0] + (mod[1] + 1) // 2
    if p == 3:
        result = mod[0]
        mins = min(mod[1], mod[2])
        result += mins
        mod[1] -= mins
        mod[2] -= mins
        mins = (mod[1]+mod[2]) // 3
        result += mins
        mins = (mod[1]+mod[2]) - mins*3
        if mins > 0:
            result += 1
    if p == 4:
        result = mod[0]
        mins = min(mod[1], mod[3])
        result += mins
        mod[1] -= mins
        mod[3] -= mins
        mins = mod[2] // 2
        result += mins
        mod[2] -= mins * 2
        mod[4] = mod[1] + mod[3]
        if mod[2]:
            if mod[4] >= 2:
                result += 1
                mod[2] = 0
                mod[4] -= 2
        mins = mod[4] // 4
        result += mins
        mod[4] -= mins * 4
        if mod[4] > 0:
            result += 1

    return result

T = int(input())
for i in range(1, T+1):
    N, P = [int(x) for x in input().split(' ')]
    G = [int(x) for x in input().split(' ')]
    print('Case #{}: {}'.format(i, solve(N, P, G)))
