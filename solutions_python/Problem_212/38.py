def rli():
    return list(map(int, input().split()))

def solve(P, G):
    A = [x % P for x in G]
    B = [0 for _ in range(P)]
    for x in A:
        B[x] += 1

    if P == 2:
        return B[0] + ((B[1] + 1) // 2)

    if P == 3:
        mi = min(B[1], B[2])
        ma = max(B[1], B[2])
        return B[0] + mi + ((ma - mi + 2) // 3)

    if P == 4:
        mi = min(B[1], B[3])
        ma = max(B[1], B[3])
        extra = (B[2] % 2) * 2 + ((ma - mi) % 4)
        if extra > 4:
            e = 2
        elif extra > 0:
            e = 1
        else:
            e = 0
        return B[0] + B[2] // 2 + mi + ((ma - mi)  // 4) + e

def read_input():
    N, P = rli()
    G = rli()
    return (P, G)

no_inputs = int(input())
inputs = [read_input() for _ in range(no_inputs)]
solutions = [solve(*inp) for inp in inputs]

for i, s in enumerate(solutions):
    print("Case #{}: {}".format(i+1, s))
