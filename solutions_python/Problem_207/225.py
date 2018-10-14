from collections import Counter
from itertools import chain

def stable_neighbors(N, R, O, Y, G, B, V):
    b = B - O
    y = Y - V
    r = R - G
    if b < 0 or y < 0 or r < 0 or (2 * max(b, y, r) > sum((b, y, r))):
        return "IMPOSSIBLE"
    if b == y == r == 0 and max(O, V, G) > sum((O, V, G)):
        return "IMPOSSIBLE"
    if b == y == r == 0 and max(O, V, G) == sum((O, V, G)):
        if O > 0:
            return "BO" * O
        if V > 0:
            return "YV" * V
        if G > 0:
            return "RG" * G

    c = Counter({"B": b, "Y": y, "R": r})
    (c1, v1), (c2, v2), (c3, v3) = c.most_common(3)
    temp = (v2 - v3) * c2 + v3 * (c2 + c3)
    result = "".join(chain(*zip(c1 * v1, temp[:v1]))) + temp[v1:]
    if O > 0 and b > 0:
        i = result.index("B")
        return result[:i] + "BO" * O + result[i:]
    if V > 0 and y > 0:
        i = result.index("Y")
        return result[:i] + "YV" * V + result[i:]
    if G > 0 and r > 0:
        i = result.index("R")
        return result[:i] + "RG" * G + result[i:]
    return result



if __name__ == "__main__":
    T = int(input())
    for i in range(T):

        N, R, O, Y, G, B, V = map(int, input().split())
        result = stable_neighbors(N, R, O, Y, G, B, V)

        print("Case #{}: {}".format(i + 1, result))
