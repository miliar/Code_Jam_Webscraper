import sys

T = int(sys.stdin.readline())
tests = []
for i in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in sys.stdin.readline().split(" ")]
    tests.append((N, R, O, Y, G, B, V))


contains = {
    "R": ["R"],
    "O": ["R", "Y"],
    "B": ["B"],
    "G": ["B", "Y"],
    "Y": ["Y"],
    "V": ["B", "R"]
}


def is_compatible(u1, u2):
    return not(u1 in contains[u2] or u2 in contains[u1])


def place_r_y_b(N, R, Y, B):
    l = [R, Y, B]
    if N > 1:
        for i in l:
            if i > N/2:
                return "IMPOSSIBLE"
    remaining = {
        "R": R,
        "Y": Y,
        "B": B
    }
    stable = []
    keys = remaining.keys()
    s_l = sorted(keys, key=lambda k: remaining[k])
    for k in s_l:
        i = 0
        while i < len(stable):
            if remaining[k] > 0:
                stable.insert(i, k)
                remaining[k] -= 1
            i += 2
        for i in range(remaining[k]):
            stable.insert(0, k)
    if N > 1:
        if stable[0] == stable[-1]:
            return "IMPOSSIBLE"
    return "".join(stable)



# def place(N, R, O, Y, G, B, V):
#     l = [R, O, Y, G, B, V]
#     if N > 1:
#         for i in l:
#             if i > N/2:
#                 return "IMPOSSIBLE"
#     remaining = {
#         "R": R,
#         "O": O,
#         "Y": Y,
#         "G": G,
#         "B": B,
#         "V": V
#     }
#     stable = []
#     keys = remaining.keys()
#     for n in range(N):
#         s_l = sorted(keys, key=lambda k: remaining[k], reverse=True)
#         for k in s_l:
#             if n == 0:
#                 stable.append(k)
#                 remaining[k] -= 1
#                 break
#             if is_compatible(stable[n-1], k):
#                 stable.append(k)
#                 remaining[k] -= 1
#                 break
#     if N > 1:
#         if not is_compatible(stable[0], stable[-1]):
#             return "IMPOSSIBLE"
#     return "".join(stable)


def place(N, R, O, Y, G, B, V):
    if N == 0:
        return ""
    if N > 1:
        if Y < V:
            return "IMPOSSIBLE"
        if R < G:
            return "IMPOSSIBLE"
        if B < O:
            return "IMPOSSIBLE"
        if B <= O and O != 0 and O+B != N:
            return "IMPOSSIBLE"
        if R <= G and G != 0 and R+G != N:
            return "IMPOSSIBLE"
        if Y <= V and Y != 0 and Y+V != N:
            return "IMPOSSIBLE"
    out1 = ""
    for i in range(O):
        out1 += "BO"
    out2 = ""
    for i in range(G):
        out2 += "RG"
    out3 = ""
    for i in range(V):
        out3 += "YV"
    N -= 2*(O+G+V)
    R -= (G)
    B -= (O)
    Y -= (V)
    s2 = place_r_y_b(N, R, Y, B)
    if s2 == "IMPOSSIBLE":
        return s2
    if len(s2) == 0:
        return out1 + out2 + out3
    if len(out2) > 0:
        for i in range(len(s2)):
            if s2[i] == "R":
                s2 = s2[:i] + out2 + s2[i:]
                break
    if len(out1) > 0:
        for i in range(len(s2)):
            if s2[i] == "B":
                s2 = s2[:i] + out1 + s2[i:]
                break
    if len(out3) > 0:
        for i in range(len(s2)):
            if s2[i] == "Y":
                s2 = s2[:i] + out3 + s2[i:]
                break
    if len(s2) > 1:
        if not(is_compatible(s2[0], s2[-1])):
            return "IMPOSSIBLE"
    return s2


for nb, t in enumerate(tests):
    res = place(*t)
    sys.stdout.write("Case #{}: {}\n".format(nb+1, res))
