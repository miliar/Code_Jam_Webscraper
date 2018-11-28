def solve(D, K):
    T = 0
    for (s, v) in K:
        T = max(T, (D - s)/v)

    return D/T

def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        D, N = F.readline().split(" ")
        K = []
        for _ in range(int(N)):
            K.append(tuple([int(e) for e in F.readline().split(" ")]))
        yield i + 1, int(D), K

out = open("A.out", "w")

#for (i, d, k) in input("Asample.in"):
#for (i, d, k) in input("A-small-attempt0.in"):
for (i, d, k) in input("A-large.in"):
    w = "Case #%d: %s" % (i, solve(d, k))
    print(w)
    print(w, file = out)
