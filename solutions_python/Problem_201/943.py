import fileinput

def r_dist(idx, s):
    dist = 0
    while s[idx + dist] != "O":
        dist += 1
    return dist - 1

def l_dist(idx, s):
    dist = 0
    while s[idx - dist] != "O":
        dist += 1
    return dist - 1

def enter(s):
    values = sorted(
            sorted(
                map(lambda x: (x, l_dist(x, s), r_dist(x, s)), filter(lambda i: s[i] != "O", range(1, len(s) - 1))),
                key=lambda x: max(x[1], x[2])),
            key=lambda x: min(x[1], x[2]))
    while len(values) > 1:
        if values[-1][1] == values[-2][1] and values[-1][2] == values[-2][2]:
            values.pop()
        else:
            break
    idx, l, r = values[-1]
    s = s[:idx] + "O" + s[idx+1:]
    return s, l, r

def simulate(N, k):
    data = "O" + "." * N + "O" 
    r = 0
    l = 0
    for i in range(k):
        data, l, r = enter(data)
        print(data)
    return (l, r)

def efficient(N, k):
    if N == k: 
        return (0,0)
    elif k == 1: 
        return (max(N - 1 - N//2, N//2), min(N - 1 - N//2, N//2))
    else:
        if N % 2 == 0:
            if k % 2 == 0:
                return efficient(N//2, k - k//2)
            else:
                return efficient(N//2 - 1, k//2)
        else:
            if k % 2 == 0:
                return efficient(N//2, k - k//2)
            else:
                return efficient(N//2, k//2)

if __name__ == "__main__":
    for case, line in enumerate(fileinput.input()):
        if case == 0:
            continue
        N, k = map(int, line.strip().split())
        print("Case #{}: {} {}".format(case, *efficient(N, k)))
