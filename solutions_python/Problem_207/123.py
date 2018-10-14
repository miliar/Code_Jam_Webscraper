import sys


def parse(instrm):
    return [int(i) for i in instrm.readline().rstrip().split()][1:]


def solve2(case):
    R, O, Y, G, B, V = case
    N = sum(case)
    if O > B or G > R or V > Y: return "IMPOSSIBLE"
    B -= O
    R -= G
    Y -= V
    ret = solve((R, 0, Y, 0, B, 0))
    if ret == "IMPOSSIBLE": return ret
    for pure, mixed, cs in ((B, O, "BO"), (R, G, "RG"), (Y, V, "YV")):
        if mixed > 0 and pure == 0:
            if 2*mixed == N: return cs*(N//2)
            return "IMPOSSIBLE"
        else:
            ret = ret.replace(cs[0], cs*mixed + cs[0], 1)
    return ret
    
    
def solve(case):
    R, _, Y, _, B, _ = case
    ns = [R, Y, B]
    cs = list("RYB")
    pairs = sorted(list(zip(ns, cs)))[::-1]
    ns, cs = list(zip(*pairs))
    ns = list(ns)
    cs = list(cs)
    if ns[0] > sum(ns[1:]): return "IMPOSSIBLE"
    sol = ""
    while ns[0] > ns[1]:
        sol += cs[0] + cs[1] + cs[0] + cs[2]
        ns[0] -= 2
        ns[1] -= 1
        ns[2] -= 1
        if any(n < 0 for n in ns): return "IMPOSSIBLE"
    while ns[1] > ns[2]:
        sol += cs[0] + cs[1]
        ns[0] -= 1
        ns[1] -= 1
    sol += "".join(cs)*ns[0]
    return sol


if __name__ == "__main__":
    with open(sys.argv[1]) as instrm:
        n = int(instrm.readline())
        for i in range(n):
            case = parse(instrm)
            ans = solve2(case)
            print("Case #{}: {}".format(i+1, ans))
